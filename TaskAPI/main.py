from fastapi import FastAPI
import uvicorn

from api.models import ApiTask, ApiTaskChange
from data_base.data_base import create_task, get_tasks, change_task, get_one_task, delete_db_task


app = FastAPI()


@app.post('/post')
async def post_tasks(task: ApiTask):
    return await create_task(task)


@app.get('/tasks')
async def get_list():
    return await get_tasks()


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    return await get_one_task(task_id)


@app.put("/tasks/{task_id}/update")
async def update_task(task_id: int, changes: ApiTaskChange):
    await change_task(task_id, changes)


@app.delete("/tasks/{task_id}/delete")
async def delete_task(task_id: int):
    return await delete_db_task(task_id)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")