#!/bin/bash
set -o errexit
set -o nounset

cd /src/backend_api && celery -A config.celery worker -l INFO
