from django.contrib import admin
from django.urls import path, include
from config.health import health_check
from projects.views import analytics_page

urlpatterns = [
    path('analytics/', analytics_page, name='analytics-page'),
    path("", health_check, name="home"),
    path("health/", health_check, name="health"),

    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/", include("projects.urls")),
    path("api/support/", include("support.urls")),

    path("projects/", include("projects.urls")),
    path("notifications/", include("notifications.urls")),
]
