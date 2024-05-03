
from celery_app import celery_app
from elasticsearch import Elasticsearch, helpers


ES_HOST = "https://es01:9200/"
ES_PASS = "y5AADXZR0l63CvTz1AsWznNiAM1Ukq7KSd3MEra"

client = Elasticsearch(
    # For local development
    hosts=[ES_HOST],
    basic_auth=('elastic', ES_PASS), 
    verify_certs=False
)


@celery_app.task(
    bind=True,
    name="ingest_data",
    autoretry_for=(),
    default_retry_delay=30,
    acks_late=True,
    task_reject_on_worker_lost=True,
)
def ingest_data(self, **kwargs):
    response = helpers.bulk(
        client,
        kwargs["docs"],
        refresh=True,
        request_timeout=60 * 10,
    )
