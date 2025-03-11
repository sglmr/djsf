"""
URL configuration for djsf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from djsf import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Homepage.as_view(), name="home"),
    path("health/", views.HealthCheck.as_view(), name="health_check"),
    path("task/", views.SimpleTask.as_view(), name="simple_task"),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(debug_toolbar_urls())
