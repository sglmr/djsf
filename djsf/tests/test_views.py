import sys
from unittest import mock

from django.test import Client
from django.urls import reverse
from gunicorn.app.wsgiapp import run
from pytest_django.asserts import assertRaisesMessage


def test_health_check_url_name():
    url = reverse("health_check")
    assert url == "/health/"


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
