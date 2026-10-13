from django.contrib import admin
from django.urls import path, include
from config.health import health_check
from config.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health_check"),
    path("", dashboard, name="home"),
]
