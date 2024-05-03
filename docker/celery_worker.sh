#!/bin/bash
echo "Starting Brussels worker"

conda run --no-capture-output -n es_ingest_worker celery -A apps.celery worker --loglevel=INFO --autoscale=1,1
