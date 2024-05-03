
from apps.celery import celery_app


@celery_app.task(
    bind=True,
    name="ingest_data",
    autoretry_for=(),
    default_retry_delay=30,
    acks_late=True,
    task_reject_on_worker_lost=True,
)
def ingest_data(self, **kwargs):
    # grab all data
    pass
