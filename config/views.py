from django.shortcuts import render
from projects.models import Project, Task
from support.models import Ticket


def dashboard(request):
    context = {
        "total_projects": Project.objects.count(),
        "active_projects": Project.objects.filter(status="ACTIVE").count(),
        "total_tasks": Task.objects.count(),
        "open_tickets": Ticket.objects.filter(
            status__in=["OPEN", "IN_PROGRESS"]
        ).count(),
        "urgent_tickets": Ticket.objects.filter(
            priority="URGENT"
        ).count(),
        "completed_tasks": Task.objects.filter(status="DONE").count(),
    }

    return render(request, "dashboard.html", context)


def admin_control(request):
    return render(request, "admin_control.html", {
        "total_projects": Project.objects.count(),
        "total_tasks": Task.objects.count(),
        "open_tickets": Ticket.objects.filter(
            status__in=["OPEN", "IN_PROGRESS"]
        ).count(),
        "urgent_tickets": Ticket.objects.filter(
            priority="URGENT"
        ).count(),
    })


def projects_page(request):
    return render(request, "projects.html")


def tasks_page(request):
    return render(request, "tasks.html")


def analytics_page(request):
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status="DONE").count()

    return render(request, "analytics.html", {
        "total_projects": total_projects,
        "active_projects": Project.objects.filter(status="ACTIVE").count(),
        "completed_projects": Project.objects.filter(
            status="COMPLETED"
        ).count(),
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "open_tickets": Ticket.objects.filter(
            status__in=["OPEN", "IN_PROGRESS"]
        ).count(),
        "urgent_tickets": Ticket.objects.filter(
            priority="URGENT"
        ).count(),
        "task_percentage": round(
            completed_tasks / total_tasks * 100
        ) if total_tasks else 0,
        "average_progress": round(
            sum(p.progress for p in Project.objects.all()) / total_projects
        ) if total_projects else 0,
    })
