from django.contrib import admin
from django.urls import path, include

from .views import (
    dashboard,
    admin_control,
    projects_page,
    tasks_page,
    analytics_page,
)

from .health import health_check

from accounts.views import role_dashboard

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path(
        "",
        dashboard,
        name="dashboard"
    ),

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "admin-control/",
        admin_control,
        name="admin-control"
    ),

    path(
        "api/auth/",
        include("accounts.urls")
    ),

    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),

    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="refresh"
    ),

    path(
        "api/",
        include("projects.urls")
    ),

    path(
        "api/support/",
        include("support.urls")
    ),

    path(
        "projects/",
        projects_page,
        name="projects-page"
    ),

    path(
        "tasks/",
        tasks_page,
        name="tasks-page"
    ),

    path(
        "analytics/",
        analytics_page,
        name="analytics-page"
    ),

    path(
        "role-dashboard/",
        role_dashboard,
        name="role-dashboard"
    ),

    path(
        "health/",
        health_check,
        name="health"
    ),

    path(
        "notifications/",
        include("notifications.urls")
    ),
]






