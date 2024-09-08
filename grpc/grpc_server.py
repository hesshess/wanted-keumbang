from concurrent import futures
import grpc
from grpc.generated import authentication_pb2_grpc
import environ

env = environ.Env()

# Import your service implementation


class AuthService(authentication_pb2_grpc.AuthServiceServicer):
    def ValidateToken(self, request, context):
        # Token validation logic
        response = authentication_pb2.TokenResponse(valid=True)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    authentication_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    # 환경 변수에서 포트 번호를 가져오거나 기본값을 설정
    grpc_port = env.int("AUTH_GRPC_PORT", default=50051)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
