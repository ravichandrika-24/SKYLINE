from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("MANAGER", "Manager"),
        ("EMPLOYEE", "Employee"),
        ("CUSTOMER", "Customer"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="EMPLOYEE")

    def __str__(self):
        return self.username
