from concurrent import futures
import grpc
from grpc.generated import authentication_pb2_grpc

# Import your service implementation


class AuthService(authentication_pb2_grpc.AuthServiceServicer):
    def ValidateToken(self, request, context):
        # Token validation logic
        response = authentication_pb2.TokenResponse(valid=True)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    authentication_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
