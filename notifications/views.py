from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def notification_page(request):

    notifications = Notification.objects.filter(
        user=request.user
    )

    unread_count = notifications.filter(
        is_read=False
    ).count()

    return render(
        request,
        "notifications.html",
        {
            "notifications": notifications,
            "unread_count": unread_count,
        }
    )


@login_required
def notification_api(request):

    notifications = Notification.objects.filter(
        user=request.user
    )[:20]

    data = []

    for notification in notifications:

        data.append({
            "id": notification.id,
            "title": notification.title,
            "message": notification.message,
            "type": notification.notification_type,
            "is_read": notification.is_read,
            "created_at": notification.created_at.isoformat(),
        })

    return JsonResponse({
        "notifications": data,
        "unread": Notification.objects.filter(
            user=request.user,
            is_read=False
        ).count(),
    })


@login_required
def mark_notifications_read(request):

    Notification.objects.filter(
        user=request.user,
        is_read=False
    ).update(
        is_read=True
    )

    return JsonResponse({
        "success": True
    })