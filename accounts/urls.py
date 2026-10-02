from django.urls import path

from .views import (
    login_page,
    register_page,
    RegisterView,
)


urlpatterns = [
    path("login/", login_page, name="login-page"),
    path("register-page/", register_page, name="register-page"),
    path("register/", RegisterView.as_view(), name="register"),
]