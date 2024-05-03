#!/bin/bash

echo "Starting Brussels server"
sleep 1
conda run --no-capture-output -n wa2_brussels alembic upgrade head
conda run --no-capture-output -n wa2_brussels gunicorn main:app
