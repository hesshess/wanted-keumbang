import os

import unittest
import grpc
from concurrent import futures
from auth_pb2 import (
    VerifyTokenRequest,
    RefreshTokenRequest,
    VerifyTokenResponse,
    RefreshTokenResponse,
    User,
)
from auth_pb2_grpc import (
    AuthServiceStub,
    add_AuthServiceServicer_to_server,
    AuthServiceServicer,
)
from grpc_server import AuthService  # 실제 gRPC 서버 클래스 가져오기


# 테스트용 Mock gRPC 서버 설정
class MockAuthService(AuthServiceServicer):
    def VerifyToken(self, request, context):
        """Mock VerifyToken 메서드"""
        token_str = request.token
        if token_str == "valid_access_token":
            return VerifyTokenResponse(
                is_valid=True, user=User(user_id="1", username="testuser", role="admin")
            )
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid or expired token.")
            return VerifyTokenResponse(is_valid=False)

    def RefreshToken(self, request, context):
        """Mock RefreshToken 메서드"""
        refresh_token_str = request.refresh_token
        if refresh_token_str == "valid_refresh_token":
            new_access_token = "new_valid_access_token"
            return RefreshTokenResponse(
                is_valid=True, new_access_token=new_access_token
            )
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid or expired refresh token.")
            return RefreshTokenResponse(is_valid=False)


class TestAuthService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # gRPC 모의 서버 생성 및 시작
        cls.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_AuthServiceServicer_to_server(MockAuthService(), cls.server)
        cls.port = "[::]:50051"  # 테스트용 포트 설정
        cls.server.add_insecure_port(cls.port)
        cls.server.start()

        # gRPC 클라이언트 생성
        cls.channel = grpc.insecure_channel("localhost:50051")
        cls.stub = AuthServiceStub(cls.channel)

    @classmethod
    def tearDownClass(cls):
        cls.server.stop(0)
        cls.channel.close()

    def test_verify_token_valid(self):
        """유효한 Access Token 검증 테스트"""
        request = VerifyTokenRequest(token="valid_access_token")
        response = self.stub.VerifyToken(request)
        self.assertTrue(response.is_valid)
        self.assertEqual(response.user.username, "testuser")

    def test_verify_token_invalid(self):
        """유효하지 않은 Access Token 검증 테스트"""
        request = VerifyTokenRequest(token="invalid_access_token")
        response = self.stub.VerifyToken(request)
        self.assertFalse(response.is_valid)

    def test_refresh_token_valid(self):
        """유효한 Refresh Token 검증 및 Access Token 재발급 테스트"""
        request = RefreshTokenRequest(refresh_token="valid_refresh_token")
        response = self.stub.RefreshToken(request)
        self.assertTrue(response.is_valid)
        self.assertEqual(response.new_access_token, "new_valid_access_token")

    def test_refresh_token_invalid(self):
        """유효하지 않은 Refresh Token 검증 테스트"""
        request = RefreshTokenRequest(refresh_token="invalid_refresh_token")
        response = self.stub.RefreshToken(request)
        self.assertFalse(response.is_valid)


if __name__ == "__main__":
    unittest.main()
