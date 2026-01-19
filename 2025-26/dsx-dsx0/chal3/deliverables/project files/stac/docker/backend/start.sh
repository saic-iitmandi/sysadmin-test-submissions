#!/bin/sh
set -e

cd /app

echo "Waiting for database to be ready..."
until python manage.py migrate --check >/dev/null 2>&1; do
  sleep 2
done

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn --config gunicorn.conf.py STAC.wsgi:application
