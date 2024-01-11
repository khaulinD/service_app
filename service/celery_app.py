import os
import time

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'service' project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

# Create a Celery instance named 'app'
app = Celery("service")

# Configure Celery using the settings from the Django project
app.config_from_object("django.conf:settings")

# Set the broker URL for Celery to use (message broker for distributed task queue)
app.conf.broker_url = settings.CELERY_BROKER_URL

# Automatically discover and register tasks from all installed apps
app.autodiscover_tasks()


# Define a Celery task named 'debug_task'
@app.task()
def debug_task():
    # Simulate a time-consuming task by sleeping for 20 seconds
    time.sleep(20)

    # Print a message to indicate the completion of the task
    print("Hello from debug_task")
