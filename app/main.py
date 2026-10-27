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


next_task_id = 2


@app.get("/health")
def get_health():
    return {
        "status": "ok",
    }


@app.get("/tasks")
def list_tasks(completed: bool | None = None):
    if completed is None:
        return tasks

    return [
        task
        for task in tasks
        if task["completed"] == completed
    ]


@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    global next_task_id

    task = {
        "id": next_task_id,
        "title": task_data.title,
        "completed": task_data.completed,
    }

    tasks.append(task)
    next_task_id += 1
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskCreate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_data.title
            task["completed"] = task_data.completed
            return task

    raise HTTPException(
        status_code=404,
        detail="任务不存在",
    )


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="任务不存在",
    )


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="任务不存在",
    )