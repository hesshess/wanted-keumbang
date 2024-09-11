import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_server.settings")

# Django가 제대로 설정되었는지 확인합니다.
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
    ) from exc

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
