#!/bin/bash
echo "Starting Brussels worker"

conda run --no-capture-output -n wa2_brussels celery -A apps.celery worker --loglevel=INFO --autoscale=1,1
