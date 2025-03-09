from django.contrib import messages
from django.http import HttpResponse
from django.views import View, generic


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
