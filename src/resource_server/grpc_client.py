import grpc
from auth_pb2 import VerifyTokenRequest, RefreshTokenRequest
from auth_pb2_grpc import AuthServiceStub


# 인증 서버에 대한 gRPC 클라이언트 생성
def verify_token(token):
    # gRPC 서버와 연결 설정
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = AuthServiceStub(channel)  # gRPC 서비스 Stub 생성
        # VerifyToken 요청 생성
        request = VerifyTokenRequest(token=token)  # 토큰 검증 요청 생성
        # 요청 전송 및 응답 수신
        response = stub.VerifyToken(request)  # 서버로부터 응답 받기
        return response


def refresh_token(refresh_token):
    # 인증 서버의 gRPC 포트 (50051)에 연결
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = AuthServiceStub(channel)
        # RefreshToken 요청 생성
        request = RefreshTokenRequest(refresh_token=refresh_token)
        # 요청 전송 및 응답 수신
        response = stub.RefreshToken(request)
        return response
