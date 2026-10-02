from django.http import JsonResponse
from django.db import connection


def health_check(request):

    database = "OK"

    try:
        connection.ensure_connection()
    except Exception:
        database = "ERROR"

    return JsonResponse(
        {
            "application": "SKYLINE",
            "status": "running",
            "database": database,
            "version": "1.0.0",
        }
    )
