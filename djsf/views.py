import logging
from time import sleep

from django.contrib import messages
from django.http import HttpResponse
from django.views import View, generic
from django_tasks import task

logger = logging.getLogger(__name__)


class Homepage(generic.TemplateView):
    """
    A simple template view.
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        messages.info(self.request, "Welcome!")
        return super().get_context_data(**kwargs)


class HealthCheck(View):
    """
    A simple health check view that returns 'healthy'.
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse("healthy")


@task
def wait_and_print():
    logger.info("I'm going to sleep")
    sleep(5)
    logger.info("I'm awake!")


class SimpleTask(View):
    """
    A simple example of a background task.
    """

    def get(self, request, *args, **kwargs):
        wait_and_print.enqueue()
        return HttpResponse("task queued!")
