import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.management import call_command

call_command("migrate", interactive=False, verbosity=1)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
