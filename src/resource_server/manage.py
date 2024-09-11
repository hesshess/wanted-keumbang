import os
import sys

# Django 설정을 먼저 로드합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resource_server.settings")

# Django가 제대로 설정되었는지 확인합니다.
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
    ) from exc

if __name__ == "__main__":
    # Django 서버 시작
    execute_from_command_line(sys.argv)
