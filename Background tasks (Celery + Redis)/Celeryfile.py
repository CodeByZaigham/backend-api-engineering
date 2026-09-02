from celery import Celery

celery_app=Celery(
     "background worker",
     broker="redis://localhost:6379/1",
     backend="redis://localhost:6379/2",
     include=["tasks"]
)
celery_app.conf.update(
     task_serializer="json",
     accept_content=["json"],
     result_serializer="json",
     timezone="UTC",
     enable_utc=True
)