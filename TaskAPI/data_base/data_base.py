from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from starlette.responses import JSONResponse

from api.models import ApiTask
from .models import Base, DB_Task
from conf import DB_CONNECT


async_engine = create_async_engine(DB_CONNECT, echo=False)

session = async_sessionmaker(async_engine)


async def create_tables() -> None:
    """
    This function creates the tables in the database
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await async_engine.dispose()


async def look_for_task(sess, task_id) -> HTTPException:
    """
    This function looks for a task in the database
    Args:
        sess: sqlalchemy session,
        task_id: task id
    Returns:
        DB_Task instance
    """
    task = await sess.get(DB_Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="This task not found")
    else:
        return task


async def create_task(task) -> JSONResponse:
    """
    This function creates the tasks in the database
    Args:
         task: DB_Task object with params id[int], title[str], description[str], status: TaskStatus
    Returns:
        JSONResponse with a status code and message
    """
    async with session() as sess:
        new_task = DB_Task(title=task.title, description=task.description)
        sess.add(new_task)
        await sess.commit()
        return JSONResponse(content={"message": "Task created successfully"}, status_code=201)


async def get_tasks() -> list:
    """
    This function returns all task
    Args:
         there are no arguments
    Returns:
       List with all tasks
    """
    async with session() as sess:
        query = select(DB_Task)
        result = await sess.execute(query)
        tasks = result.scalars().all()
        return tasks


async def get_one_task(task_id: int) -> DB_Task:
    """
    This function returns one task by id
    Args:
         task_id(int): primary key
    Returns:
        DB_Task instance
    """
    async with session() as sess:
        task = await look_for_task(sess, task_id)
        return task


async def change_task(task_id, changes) -> None:
    """
    This function changes one task by id
    Args:
         task_id(int): primary key
         changes(dict): changes dict
    """
    async with session() as sess:
        task = await look_for_task(sess, task_id)
        new_data = dict(changes)

        if new_data["status"] == None:
            new_data.pop("status")
        else:
            setattr(task, "status", new_data["status"].name)
            new_data.pop("status")

        for key, value in new_data.items():
            setattr(task, key, value)
        await sess.commit()


async def delete_db_task(task_id) -> JSONResponse:
    """
    This function deletes one task by id
    Args:
         task_id(int): primary key
    Returns:
        JSONResponse with a status code and message
    """
    async with session() as sess:
        task = await look_for_task(sess, task_id)
        await sess.delete(task)
        await sess.commit()
        return JSONResponse(content={"message": "The task was successfully deleted"}, status_code=200)
