from fastapi import FastAPI
from celery.result import AsyncResult
from Celeryfile import celery_app
from tasks import process_task

app=FastAPI()

@app.post("/process")
def process(data: str):

     task = process_task.delay(data)

     return {
          "task_id": task.id,
          "status": "Task submitted"
     }

@app.get("/task/{task_id}")
def get_task_status(task_id: str):

     task = AsyncResult(task_id, app=celery_app)

     return {
          "task_id": task_id,
          "status": task.status,
          "result": task.result if task.successful() else None
     }