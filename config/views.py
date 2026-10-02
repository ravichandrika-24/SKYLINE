from django.shortcuts import render

from projects.models import Project, Task
from support.models import Ticket


def dashboard(request):

    total_projects = Project.objects.count()

    active_projects = Project.objects.filter(
        status="ACTIVE"
    ).count()

    total_tasks = Task.objects.count()

    open_tickets = Ticket.objects.filter(
        status__in=["OPEN", "IN_PROGRESS"]
    ).count()

    urgent_tickets = Ticket.objects.filter(
        priority="URGENT"
    ).count()

    completed_tasks = Task.objects.filter(
        status="DONE"
    ).count()

    context = {
        "total_projects": total_projects,
        "active_projects": active_projects,
        "total_tasks": total_tasks,
        "open_tickets": open_tickets,
        "urgent_tickets": urgent_tickets,
        "completed_tasks": completed_tasks,
    }

    return render(
        request,
        "dashboard.html",
        context
    )


def admin_control(request):

    context = {
        "total_projects": Project.objects.count(),

        "total_tasks": Task.objects.count(),

        "open_tickets": Ticket.objects.filter(
            status__in=["OPEN", "IN_PROGRESS"]
        ).count(),

        "urgent_tickets": Ticket.objects.filter(
            priority="URGENT"
        ).count(),
    }

    return render(
        request,
        "admin_control.html",
        context
    )


def projects_page(request):

    return render(
        request,
        "projects.html"
    )


def tasks_page(request):

    return render(
        request,
        "tasks.html"
    )


def analytics_page(request):

    total_projects = Project.objects.count()

    active_projects = Project.objects.filter(
        status="ACTIVE"
    ).count()

    completed_projects = Project.objects.filter(
        status="COMPLETED"
    ).count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status="DONE"
    ).count()

    open_tickets = Ticket.objects.filter(
        status__in=["OPEN", "IN_PROGRESS"]
    ).count()

    urgent_tickets = Ticket.objects.filter(
        priority="URGENT"
    ).count()

    if total_tasks > 0:

        task_percentage = round(
            completed_tasks / total_tasks * 100
        )

    else:

        task_percentage = 0

    if total_projects > 0:

        projects = Project.objects.all()

        average_progress = round(
            sum(
                project.progress
                for project in projects
            ) / total_projects
        )

    else:

        average_progress = 0

    context = {
        "total_projects": total_projects,
        "active_projects": active_projects,
        "completed_projects": completed_projects,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "open_tickets": open_tickets,
        "urgent_tickets": urgent_tickets,
        "task_percentage": task_percentage,
        "average_progress": average_progress,
    }

    return render(
        request,
        "analytics.html",
        context
    )