import os
import django

# Django settings 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_server.settings")
django.setup()

import grpc
from concurrent import futures
from auth_pb2 import (
    VerifyTokenResponse,
    RefreshTokenResponse,
    User,
)  # gRPC 메시지 정의 가져오기
from auth_pb2_grpc import (
    AuthServiceServicer,
    add_AuthServiceServicer_to_server,
)  # gRPC 서비스 정의 가져오기
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
import logging

# 로그 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# gRPC 서버 포트 상수 정의
GRPC_PORT = 50051


# gRPC 서버 클래스 정의
class AuthService(AuthServiceServicer):
    def VerifyToken(self, request, context):
        """JWT 토큰의 유효성을 검증하고 사용자 정보를 반환하는 메서드"""
        token_str = request.token
        try:
            # JWT 토큰의 유효성 검증
            token = AccessToken(token_str)

            # user 정보를 추출
            user_id = token["user_id"]
            username = token["username"]
            role = token["role"]

            logger.info(f"Token verified successfully for user: {username}")

            return VerifyTokenResponse(
                is_valid=True, user=User(user_id=user_id, username=username, role=role)
            )
        except Exception as e:
            # 토큰이 유효하지 않거나 예외 발생 시 처리
            logger.error(f"Token verification failed: {e}")
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details(str(e))
            return VerifyTokenResponse(is_valid=False)

    def RefreshToken(self, request, context):
        """Refresh Token을 검증하고 새로운 Access Token을 발급하는 메서드"""
        refresh_token_str = request.refresh_token
        try:
            # Refresh Token의 유효성 검증
            refresh_token = RefreshToken(refresh_token_str)

            # 새로운 Access Token 생성
            new_access_token = str(refresh_token.access_token)
            logger.info("New Access Token generated successfully.")
            return RefreshTokenResponse(
                is_valid=True, new_access_token=new_access_token
            )
        except Exception as e:
            logger.error(f"Refresh token validation failed: {e}")
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details(str(e))
            return RefreshTokenResponse(is_valid=False)


# gRPC 서버 시작 함수 정의
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port(f"[::]:{GRPC_PORT}")  # 인증 서버의 gRPC 포트 설정
    server.start()
    logger.info(f"Auth gRPC Server started at port {GRPC_PORT}.")
    server.wait_for_termination()


if __name__ == "__main__":
    logger.info("Starting gRPC server...")
    serve()
