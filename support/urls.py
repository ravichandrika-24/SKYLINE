from django.urls import path

from .views import (
    ticket_page,
    ticket_management_page,
    TicketListCreateView,
)


urlpatterns = [

    path(
        "",
        ticket_page,
        name="ticket-page"
    ),

    path(
        "tickets/",
        TicketListCreateView.as_view(),
        name="tickets"
    ),

    path(
        "management/",
        ticket_management_page,
        name="ticket-management"
    ),
]