from django.db import models
from django.utils import timezone


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("ORDERED", "주문 완료"),
        ("PAID", "입금 완료"),
        ("SHIPPED", "발송 완료"),
        ("RECEIVED", "수령 완료"),
    ]

    order_id = models.CharField(max_length=20, unique=True)  # 주문 번호, 자동 생성
    order_date = models.DateTimeField(
        default=timezone.now
    )  # 주문 일자, 현재 시간으로 설정
    customer = models.ForeignKey(
        "User", on_delete=models.CASCADE
    )  # 주문자, Users 테이블 참조
    status = models.CharField(
        max_length=10, choices=ORDER_STATUS_CHOICES, default="ORDERED"
    )  # 주문 상태
    item = models.ForeignKey(
        "Product", on_delete=models.CASCADE
    )  # 품목, Products 테이블 참조
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # 수량 (그램 단위, 소수점 둘째 자리까지)
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # 금액
    shipping_address = models.CharField(max_length=255)  # 배송지 정보

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.username}"
