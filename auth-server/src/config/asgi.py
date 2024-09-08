import os
from django.core.asgi import get_asgi_application
from django_grpc_framework import util
from authentication.grpc import AuthService

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_server.settings")

django_application = get_asgi_application()

# gRPC 애플리케이션 설정
grpc_application = util.create_grpc_server((AuthService,))


async def application(scope, receive, send):
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "grpc":
        await grpc_application(scope, receive, send)
