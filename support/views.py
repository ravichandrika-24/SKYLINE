from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from .models import Ticket
from .ai import analyze_ticket
from notifications.utils import create_notification


def ticket_page(request):

    result = None
    saved = False

    if request.method == "POST":

        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title and description:

            result = analyze_ticket(
                title,
                description
            )

            if request.user.is_authenticated:

                ticket = Ticket.objects.create(
                    customer=request.user,
                    title=title,
                    description=description,
                    category=result["category"],
                    priority=result["priority"],
                    ai_summary=result["summary"],
                )

                create_notification(
                    user=request.user,
                    title="AI Support Ticket Created",
                    message=(
                        f"Ticket '{ticket.title}' created. "
                        f"Category: {ticket.category}. "
                        f"Priority: {ticket.priority}."
                    ),
                    notification_type="AI_SUPPORT",
                )

                saved = True

    return render(
        request,
        "support/tickets.html",
        {
            "result": result,
            "saved": saved,
        }
    )


def ticket_management_page(request):

    tickets = Ticket.objects.all().order_by("-created_at")

    search = request.GET.get("search", "").strip()
    priority = request.GET.get("priority", "").strip()
    status = request.GET.get("status", "").strip()

    if search:
        tickets = tickets.filter(
            title__icontains=search
        )

    if priority:
        tickets = tickets.filter(
            priority=priority
        )

    if status:
        tickets = tickets.filter(
            status=status
        )

    return render(
        request,
        "support/ticket_management.html",
        {
            "tickets": tickets,
            "search": search,
            "priority": priority,
            "status": status,
        }
    )


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketListCreateView(
    generics.ListCreateAPIView
):

    queryset = Ticket.objects.all().order_by(
        "-created_at"
    )

    serializer_class = TicketSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(self, serializer):

        title = serializer.validated_data["title"]
        description = serializer.validated_data["description"]

        result = analyze_ticket(
            title,
            description
        )

        ticket = serializer.save(
            customer=self.request.user,
            category=result["category"],
            priority=result["priority"],
            ai_summary=result["summary"],
        )

        create_notification(
            user=self.request.user,
            title="AI Support Ticket Created",
            message=(
                f"'{ticket.title}' classified as "
                f"{ticket.category} / {ticket.priority}."
            ),
            notification_type="AI_SUPPORT",
        )
