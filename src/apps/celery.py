import os

from celery import Celery

celery_app = Celery(
    "tasks",
    broker="amqp://{rabbitmq_login}:{rabbitmq_pass}@{rabbitmq_host}//".format(
        rabbitmq_login=os.environ["RABBITMQ_LOGIN"],
        rabbitmq_pass=os.environ["RABBITMQ_PASS"],
        rabbitmq_host=os.environ["RABBITMQ_HOST"],
    ),
    include=["apps.crawler.tasks"],
)
