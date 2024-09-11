import grpc
from concurrent import futures
from auth_pb2 import VerifyTokenResponse, User  # 절대 경로로 수정
from auth_pb2_grpc import (
    AuthServiceServicer,
    add_AuthServiceServicer_to_server,
)  # 절대 경로로 수정


# gRPC 서버 클래스 정의
class ResourceService(AuthServiceServicer):
    # 자원 서버 관련 메서드 구현
    pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AuthServiceServicer_to_server(ResourceService(), server)
    server.add_insecure_port("[::]:50052")  # 자원 서버의 gRPC 포트를 50052로 설정
    server.start()
    print("Resource gRPC Server started at port 50052.")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
