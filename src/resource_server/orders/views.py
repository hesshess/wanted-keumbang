from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Order, Invoice
from .serializers import OrderSerializer, InvoiceSerializer
from grpc_client import verify_token, refresh_token  # gRPC 클라이언트 추가


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def get_queryset(self):
        # JWT 토큰을 헤더에서 가져옴
        token = self.request.headers.get("Authorization").split(" ")[1]
        # gRPC 클라이언트로 인증 서버에 토큰 검증 요청
        response = verify_token(token)

        if response.is_valid:
            # 인증이 유효한 경우, 현재 요청한 사용자가 만든 주문만 반환
            user = response.user.username  # gRPC 응답의 사용자 정보를 사용
            return Order.objects.filter(customer_name=user)
        else:
            # 토큰이 유효하지 않은 경우
            return Order.objects.none()

    def list(self, request, *args, **kwargs):
        # JWT 토큰을 헤더에서 가져옴
        token = request.headers.get("Authorization").split(" ")[1]
        # gRPC 클라이언트로 인증 서버에 토큰 검증 요청
        response = verify_token(token)

        if response.is_valid:
            # 유효한 경우, 기존 로직 수행
            return super().list(request, *args, **kwargs)
        else:
            # 토큰이 유효하지 않은 경우, Refresh Token 사용
            refresh_token_str = request.headers.get("Authorization").split(" ")[1]
            refresh_response = refresh_token(refresh_token_str)
            if refresh_response.is_valid:
                # 새로운 Access Token을 응답 헤더에 추가
                response = super().list(request, *args, **kwargs)
                response["Authorization"] = (
                    f"Bearer {refresh_response.new_access_token}"
                )
                return response
            else:
                # Refresh Token도 유효하지 않으면 401 에러 반환
                return Response(
                    {"error": "Invalid token or refresh token expired"}, status=401
                )


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # JWT 토큰을 헤더에서 가져옴
        token = self.request.headers.get("Authorization").split(" ")[1]
        # gRPC 클라이언트로 인증 서버에 토큰 검증 요청
        response = verify_token(token)

        if response.is_valid:
            # 인증이 유효한 경우, 현재 요청한 사용자가 만든 주문의 인보이스만 반환
            user = response.user.username  # gRPC 응답의 사용자 정보를 사용
            return Invoice.objects.filter(order__customer_name=user)
        else:
            # 토큰이 유효하지 않은 경우
            return Invoice.objects.none()
