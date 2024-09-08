import grpc
from authentication.models import CustomUser
from authentication.serializers import UserSerializer
from authentication.proto import auth_pb2, auth_pb2_grpc
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User


class AuthService(auth_pb2_grpc.AuthServicer):
    def VerifyToken(self, request, context):
        try:
            token = AccessToken(request.accessToken)
            user_id = token["user_id"]
            user = User.objects.get(id=user_id)
            user_data = UserSerializer(user).data
            return auth_pb2.VerifyTokenResponse(
                isValid=True,
                user=auth_pb2.User(
                    userId=str(user.id),
                    username=user.username,
                    role="user",  # 역할을 정의하는 로직 추가 가능
                ),
            )
        except Exception as e:
            return auth_pb2.VerifyTokenResponse(isValid=False)
