#!/bin/bash
echo "Starting Brussels worker"

conda run --no-capture-output -n es_tripadvisor_nyc celery -A apps.celery worker --loglevel=INFO --autoscale=1,1
