from django.http import JsonResponse
from django.db import connection
from django.core.management import call_command
from io import StringIO

def dbcheck(request):
    result = {}

    try:
        result["tables_before"] = connection.introspection.table_names()

        out = StringIO()
        call_command("showmigrations", "projects", stdout=out, stderr=out)
        result["migrations"] = out.getvalue()

        call_command("migrate", interactive=False, verbosity=1)

        result["tables_after"] = connection.introspection.table_names()
        result["projects_table_exists"] = "projects_project" in result["tables_after"]

    except Exception as e:
        result["error"] = type(e).__name__
        result["message"] = str(e)

    return JsonResponse(result)
