#!/usr/bin/env python
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalproject.settings")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


    django.setup()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

