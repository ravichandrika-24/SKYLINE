from django.urls import path

from .views import (
    notification_page,
    notification_api,
    mark_notifications_read,
)


urlpatterns = [

    path(
        "",
        notification_page,
        name="notifications"
    ),

    path(
        "api/",
        notification_api,
        name="notification-api"
    ),

    path(
        "read/",
        mark_notifications_read,
        name="notifications-read"
    ),
]