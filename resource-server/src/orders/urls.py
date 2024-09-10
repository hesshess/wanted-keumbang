from django.urls import path
from .views import (
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
    OrderStatusUpdateAPIView,
)

urlpatterns = [
    path(
        "orders/", OrderListCreateAPIView.as_view(), name="order-list-create"
    ),  # 주문 목록 조회 및 주문 생성
    path(
        "orders/<uuid:pk>/",
        OrderRetrieveUpdateDestroyAPIView.as_view(),
        name="order-detail",
    ),  # 특정 주문 조회, 수정, 삭제
    path(
        "orders/<uuid:pk>/status/",
        OrderStatusUpdateAPIView.as_view(),
        name="order-status-update",
    ),  # 주문 상태 변경
]
