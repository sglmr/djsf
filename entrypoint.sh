#!/bin/bash
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --ignore tailwind_input.css

# Start server
echo "Starting server..."
exec gunicorn nib.wsgi:application --config gunicorn.conf.py