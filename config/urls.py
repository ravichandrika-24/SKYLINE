from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from config.health import health_check


def home(request):
    return JsonResponse({
        "application": "SKYLINE",
        "status": "running",
        "message": "SKYLINE AI Business Operations Platform",
        "version": "1.0.0"
    })


urlpatterns = [
    path("", home, name="home"),
    path("health/", health_check, name="health"),

    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/", include("projects.urls")),
    path("api/support/", include("support.urls")),

    path("projects/", include("projects.urls")),
    path("notifications/", include("notifications.urls")),
]
