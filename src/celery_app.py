import os

from celery import Celery

celery_app = Celery(
    "tasks",
    broker="amqp://{rabbitmq_login}:{rabbitmq_pass}@{rabbitmq_host}//".format(
        rabbitmq_login="guest",
        rabbitmq_pass="guest",
        rabbitmq_host=os.environ["RABBITMQ_HOST"],
    ),
    include=["apps.crawler.tasks"],
)
