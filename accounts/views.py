from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer


def login_page(request):
    return render(request, "accounts/login.html")


def register_page(request):
    return render(request, "accounts/register.html")


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


def role_dashboard(request):

    if not request.user.is_authenticated:
        return redirect("/api/auth/login/")

    role = request.user.role

    if role == "ADMIN":
        page = "Admin"
    elif role == "MANAGER":
        page = "Manager"
    elif role == "EMPLOYEE":
        page = "Employee"
    else:
        page = "Customer"

    return render(
        request,
        "role_dashboard.html",
        {
            "user": request.user,
            "role": role,
            "page": page,
        }
    )