from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

from notifications.utils import create_notification


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.role in ["ADMIN", "MANAGER"]:
            return Project.objects.all().order_by("-created_at")

        return Project.objects.filter(
            manager=user
        ).order_by("-created_at")

    def perform_create(self, serializer):

        project = serializer.save()

        create_notification(
            user=self.request.user,
            title="New Project Created",
            message=f"Project '{project.name}' was created successfully.",
            notification_type="PROJECT"
        )


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.role in ["ADMIN", "MANAGER"]:
            return Task.objects.all().order_by("-created_at")

        return Task.objects.filter(
            assigned_to=user
        ).order_by("-created_at")

    def perform_create(self, serializer):

        task = serializer.save()

        if task.assigned_to:

            create_notification(
                user=task.assigned_to,
                title="New Task Assigned",
                message=f"You have been assigned task '{task.title}'.",
                notification_type="TASK"
            )