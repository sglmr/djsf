
# Variables
python := ".venv/bin/python"

# Default
default:
    just --list

# === Django Commands ===

# Make Django migrations
makemigrations:
    {{python}} manage.py makemigrations

# Perform all Django migrations
migrate: makemigrations
    {{python}} manage.py migrate

# Run the development server
run:
    {{python}} manage.py runserver

# collect static files
collectstatic:
    {{python}} manage.py collectstatic --no-input

# Enter the Django shell
shell:
    {{python}} manage.py shell

# Run worker to process tasks
worker:
    {{python}} manage.py qcluster

# === Testing & Dependency Management ===

# run pytest
test: collectstatic
    uv run pytest --cov=djsf

# Check for outdated depndencies
audit:
    {{python}} manage.py check
    uv pip list --outdated

# Upgrade dependencies (& test)
upgrade:
    uv sync --upgrade
    just test



# === Production ===

# Connect to the VPS server
connect:
    ssh dok2

# Deploy to dokku VPS server
deploy:
    git push dokku main