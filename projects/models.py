from django.db import models
from accounts.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="managed_projects")
    status = models.CharField(
        max_length=30,
        choices=[
            ("PLANNING", "Planning"),
            ("ACTIVE", "Active"),
            ("COMPLETED", "Completed"),
        ],
        default="PLANNING"
    )
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks"
    )
    status = models.CharField(
        max_length=30,
        choices=[
            ("TODO", "To Do"),
            ("PROGRESS", "In Progress"),
            ("DONE", "Done"),
        ],
        default="TODO"
    )
    priority = models.CharField(
        max_length=20,
        choices=[
            ("LOW", "Low"),
            ("MEDIUM", "Medium"),
            ("HIGH", "High"),
        ],
        default="MEDIUM"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
