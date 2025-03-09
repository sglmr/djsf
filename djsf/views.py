from django.http import HttpResponse
from django.views import View


class HealthCheck(View):
    """
    A simple health check view that returns 'healthy'.
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse("healthy")
