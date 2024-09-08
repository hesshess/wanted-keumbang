import os
import sys
from concurrent import futures
import grpc

# 현재 디렉토리의 부모 디렉토리 (src 디렉토리)를 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Django 환경 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

from authentication.proto import auth_pb2_grpc  # 컴파일된 파일에서 import
from authentication.grpc_service import AuthService  # 순환 import 문제 해결 후 import


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server is running on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
