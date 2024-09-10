from django.db import models
from products.models import (
    Product,
    Price,
)  # Product와 Price 모델을 참조하기 위해 import


class Order(models.Model):
    """
    주문을 정의하는 모델입니다.
    """

    ORDER_STATUS_CHOICES = [
        ("ORDER_PLACED", "Order Placed"),
        ("PAYMENT_COMPLETED", "Payment Completed"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
    ]

    order_id = models.AutoField(primary_key=True)  # 주문 고유 식별자 (자동 증가)
    order_date = models.DateTimeField(auto_now_add=True)  # 주문 생성 시간
    customer_name = models.CharField(max_length=255)  # 주문자 이름
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default="ORDER_PLACED"
    )  # 주문 상태
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품 외래 키
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # 수량 (그램 단위)
    price = models.ForeignKey(
        Price, on_delete=models.SET_NULL, null=True
    )  # 가격 외래 키 (주문 당시 가격 참조)
    order_price = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # 주문 당시의 그램당 가격
    total_price = models.DecimalField(
        max_digits=15, decimal_places=2
    )  # 총 금액 (order_price * quantity)
    shipping_address = models.TextField()  # 배송지 정보
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name}"

    def save(self, *args, **kwargs):
        """
        주문 가격과 총 금액을 설정하는 로직 (주문 당시 가격을 기반으로)
        """
        if self.price:
            self.order_price = self.price.price_per_gram
            self.total_price = self.order_price * self.quantity
        super().save(*args, **kwargs)
