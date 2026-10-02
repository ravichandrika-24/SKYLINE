from django.db import models
from accounts.models import User

class Ticket(models.Model):
    CATEGORY_CHOICES = (
        ("TECHNICAL", "Technical"),
        ("PAYMENT", "Payment"),
        ("ACCOUNT", "Account"),
        ("OTHER", "Other"),
    )

    PRIORITY_CHOICES = (
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("URGENT", "Urgent"),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="OTHER")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="MEDIUM")
    status = models.CharField(
        max_length=30,
        choices=[
            ("OPEN", "Open"),
            ("IN_PROGRESS", "In Progress"),
            ("RESOLVED", "Resolved"),
        ],
        default="OPEN"
    )
    ai_summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
