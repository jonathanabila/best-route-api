#!/bin/bash
service ssh start
set -e

cd src && newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT -k gevent wsgi:app
