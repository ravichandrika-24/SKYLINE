from .models import Ticket


def analyze_ticket(title, description):

    text = (title + " " + description).lower()

    if any(word in text for word in [
        "payment",
        "refund",
        "charged",
        "transaction",
        "money",
        "billing"
    ]):
        category = "PAYMENT"

    elif any(word in text for word in [
        "password",
        "login",
        "error",
        "bug",
        "crash",
        "technical",
        "website",
        "app"
    ]):
        category = "TECHNICAL"

    elif any(word in text for word in [
        "account",
        "profile",
        "username",
        "email"
    ]):
        category = "ACCOUNT"

    else:
        category = "OTHER"


    if any(word in text for word in [
        "urgent",
        "critical",
        "down",
        "blocked",
        "cannot access",
        "not working",
        "security"
    ]):
        priority = "URGENT"

    elif any(word in text for word in [
        "error",
        "failed",
        "failure",
        "problem",
        "issue"
    ]):
        priority = "HIGH"

    elif any(word in text for word in [
        "slow",
        "delay",
        "waiting"
    ]):
        priority = "MEDIUM"

    else:
        priority = "LOW"


    words = description.split()

    summary = " ".join(words[:25])

    if len(words) > 25:
        summary += "..."


    if priority == "URGENT":
        recommendation = (
            "Immediately assign this ticket to a support manager "
            "and investigate the issue."
        )

    elif priority == "HIGH":
        recommendation = (
            "Assign this ticket to a technical support employee "
            "for quick investigation."
        )

    elif category == "PAYMENT":
        recommendation = (
            "Verify the customer's transaction and payment records."
        )

    elif category == "ACCOUNT":
        recommendation = (
            "Verify the customer's account information and access."
        )

    else:
        recommendation = (
            "Review the ticket and assign it to the appropriate team."
        )


    return {
        "category": category,
        "priority": priority,
        "summary": summary,
        "recommendation": recommendation,
    }


def create_ai_ticket(customer, title, description):

    result = analyze_ticket(
        title,
        description
    )

    return Ticket.objects.create(
        customer=customer,
        title=title,
        description=description,
        category=result["category"],
        priority=result["priority"],
        ai_summary=result["summary"],
    )