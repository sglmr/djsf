import multiprocessing

from environs import env

# Read the environment variables
env.read_env()

# Server socket
port = env.str("PORT", "8000")
bind = f"0.0.0.0:{port}"  # IP and port to bind

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
# worker_class = "gevent"  # Options: sync, eventlet, gevent, tornado, gthread
# timeout = 30  # Seconds before a worker is killed and restarted

max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "-"  # Log to stdout
errorlog = "-"  # Log to stderr
loglevel = "info"  # Options: debug, info, warning, error, critical

# Django specific settings
django_settings = "djsf.settings"  # Replace with your Django settings module

# Process naming
proc_name = "djsf"
