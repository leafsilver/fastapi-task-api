from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=100,
    )
    completed: bool = False


app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "学习 FastAPI",
        "completed": False,
    },
]


@app.get("/health")
def get_health():
    return {
        "status": "ok",
    }


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    task = {
        "id": len(tasks) + 1,
        "title": task_data.title,
        "completed": task_data.completed,
    }

    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="任务不存在",
    )