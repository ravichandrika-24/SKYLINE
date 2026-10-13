
from django.contrib import admin
from django.urls import path, include

from config.health import health_check
from config.views import dashboard

urlpatterns = [
    # Main website dashboard
    path("", dashboard, name="home"),

    # Health check
    path("health/", health_check, name="health"),

    # Django admin
    path("admin/", admin.site.urls),

    # Authentication APIs
    path("api/auth/", include("accounts.urls")),

    # Projects and tasks
    path("api/", include("projects.urls")),
    path("projects/", include("projects.urls")),

    # Support tickets
    path("api/support/", include("support.urls")),

    # Notifications
    path("notifications/", include("notifications.urls")),
]
