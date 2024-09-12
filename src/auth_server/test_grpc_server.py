import unittest
import requests  # REST API 호출을 위한 requests 라이브러리
import grpc
from auth_pb2 import (
    VerifyTokenRequest,
    RefreshTokenRequest,
    VerifyTokenResponse,
    RefreshTokenResponse,
)
from auth_pb2_grpc import AuthServiceStub


class TestAuthService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Django REST API 서버 URL (auth_server의 Django 서버)
        cls.base_url = "http://localhost:8888"

        # 사용자 등록 및 로그인 API를 호출하여 유효한 토큰을 생성
        cls.access_token, cls.refresh_token = cls.register_and_login_user()

        # gRPC 클라이언트 생성
        cls.channel = grpc.insecure_channel("localhost:50051")
        cls.stub = AuthServiceStub(cls.channel)

    @classmethod
    def register_and_login_user(cls):
        # 사용자 등록
        register_response = requests.post(
            f"{cls.base_url}/auth/register/",
            json={"username": "testuser9", "password": "testpassword"},
        )
        if register_response.status_code != 201:
            raise Exception(
                "User registration failed. Make sure the server is running and the endpoint is correct."
            )

        # 사용자 로그인 및 토큰 발급
        login_response = requests.post(
            f"{cls.base_url}/auth/login/",
            json={"username": "testuser", "password": "testpassword"},
        )
        if login_response.status_code != 200:
            raise Exception(
                "User login failed. Make sure the server is running and the endpoint is correct."
            )

        data = login_response.json()
        return data["access"], data["refresh"]

    @classmethod
    def tearDownClass(cls):
        # gRPC 채널 닫기
        cls.channel.close()

    def test_verify_token_valid(self):
        """유효한 Access Token 검증 테스트"""
        request = VerifyTokenRequest(token=self.access_token)
        response = self.stub.VerifyToken(request)
        self.assertTrue(response.is_valid)

    def test_refresh_token_valid(self):
        """유효한 Refresh Token 검증 및 Access Token 재발급 테스트"""
        request = RefreshTokenRequest(refresh_token=self.refresh_token)
        response = self.stub.RefreshToken(request)
        self.assertTrue(response.is_valid)
        self.assertIsNotNone(
            response.new_access_token
        )  # 새로운 Access Token이 존재하는지 확인


if __name__ == "__main__":
    unittest.main()
