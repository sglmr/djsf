import sys
from http import HTTPStatus
from unittest import mock

from django.conf import settings
from django.test import Client
from django.urls import resolve, reverse
from gunicorn.app.wsgiapp import run
from pytest_django.asserts import assertRaisesMessage, assertTemplateUsed

from .. import views

# ----------------------------------------------------------
#       Home page view tests
# ----------------------------------------------------------


def test_home_url_name():
    url = reverse("home")
    assert url == ("/")


def test_home_status_ok(client: Client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_home_template_used(client: Client):
    url = reverse("home")
    response = client.get(url)
    assertTemplateUsed(response, "home.html")


def test_home_resolves_the_correct_view():
    view = resolve("/")
    assert view.func.view_class == views.Homepage


def test_settings_testing():
    assert settings.TESTING is True


def test_health_check_url_name():
    url = reverse("health_check")
    assert url == "/health/"


# ----------------------------------------------------------
#       Misc. Tests
# ----------------------------------------------------------


def test_health_check_http_status_ok(client: Client):
    response = client.get("/health/")
    assert response.status_code == 200


def test_gunicorn_config():
    # https://adamj.eu/tech/2021/12/29/set-up-a-gunicorn-configuration-file-and-test-it/
    argv = [
        "gunicorn",
        "--check-config",
        "--config",
        "gunicorn.conf.py",
        "djsf.wsgi",
    ]
    mock_argv = mock.patch.object(sys, "argv", argv)

    with assertRaisesMessage(SystemExit, "") as cm, mock_argv:
        run()

    exit_code = cm.exception.args[0]
    assert exit_code == 0
