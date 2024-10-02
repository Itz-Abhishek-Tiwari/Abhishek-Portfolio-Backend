#!/bin/bash
# Collect static files
python3 manage.py collectstatic --noinput

# Run database migrations
python3 manage.py migrate
