from django.http import JsonResponse
import traceback
from .views import dashboard, analytics_page

def diagnose(request):
    result = {}
    for name, view in [("dashboard", dashboard), ("analytics", analytics_page)]:
        try:
            response = view(request)
            result[name] = {"status": response.status_code}
        except Exception as e:
            result[name] = {
                "error": type(e).__name__,
                "message": str(e),
                "traceback": traceback.format_exc()
            }
    return JsonResponse(result)
