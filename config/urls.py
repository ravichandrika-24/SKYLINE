from django.contrib import admin
from django.urls import path, include
from config.health import health_check
from config.views import dashboard, admin_control, projects_page, tasks_page, analytics_page

urlpatterns = [
    path("", dashboard, name="home"),
    path("health/", health_check, name="health"),

    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/", include("projects.urls")),
    path("api/support/", include("support.urls")),

    path("projects/", projects_page, name="projects-page"),
    path("tasks/", tasks_page, name="tasks-page"),
    path("analytics/", analytics_page, name="analytics-page"),
    path("admin-control/", admin_control, name="admin-control"),

    path("notifications/", include("notifications.urls")),
]
