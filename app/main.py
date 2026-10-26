from fastapi import FastAPI, HTTPException


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


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="任务不存在",
    )
