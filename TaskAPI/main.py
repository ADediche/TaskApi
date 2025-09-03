import asyncio

from fastapi import FastAPI

from api.models import Task
from data_base.data_base import create_tables, create_task


app = FastAPI()


@app.post('/post')
async def create_tasks(task: Task):
    return None


@app.get('/tasks')
async def get_list():
    return {'message': f'Hello World!!! {get_list}'}


@app.get("/tasks/{task_id}")
async def get_task(task_id):
    return {'message': f'Hello World!!! {task_id}'}


@app.patch("/tasks/{task_id}")
async def update_task(task_id, task: Task):
    return {'message': f'Hello World!!! {task_id}'}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id):
    return {'message': f'Hello World!!! {task_id}'}


asyncio.run(create_tables())
asyncio.run(create_task())