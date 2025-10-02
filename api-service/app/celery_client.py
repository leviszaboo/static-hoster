import os

from celery import Celery

celery = Celery(
    "api-service",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)
