"""
URL configuration for djsf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path

from djsf import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", views.HealthCheck.as_view(), name="health_check"),
    path("__reload__/", include("django_browser_reload.urls")),
]
