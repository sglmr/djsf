import logging
from time import sleep

from django.contrib import messages
from django.http import HttpResponse
from django.views import View, generic
from django_q.tasks import async_task

logger = logging.getLogger(__name__)


class Homepage(generic.TemplateView):
    """
    A simple template view.
    """

    template_name = "home.html"
    extra_context = {"page_title": "Home"}

    def get_context_data(self, **kwargs):
        messages.info(self.request, "Welcome!")
        return super().get_context_data(**kwargs)


class HealthCheck(View):
    """
    A simple health check view that returns 'healthy'.
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse("healthy")


def wait_and_print() -> None:
    logger.info("I'm going to sleep")
    sleep(5)
    logger.info("I'm awake!")


class SimpleTask(View):
    """
    A simple example of a background task.
    """

    def get(self, request, *args, **kwargs):
        async_task(wait_and_print)
        return HttpResponse("task queued!")
