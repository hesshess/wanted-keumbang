from django.db import models
from products.models import Product, Price  # 수정: products 앱의 모델을 임포트


class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ("BUY", "구매 주문"),  # 소비자가 금을 구매하는 주문
        ("SELL", "판매 주문"),  # 소비자가 금을 판매하는 주문
    ]

    BUY_ORDER_STATUS_CHOICES = [
        ("ORDER_PLACED", "주문 완료"),
        ("PAYMENT_COMPLETED", "입금 완료"),
        ("SHIPPED", "발송 완료"),
    ]

    SELL_ORDER_STATUS_CHOICES = [
        ("ORDER_PLACED", "주문 완료"),
        ("TRANSFERRED", "송금 완료"),
        ("RECEIVED", "수령 완료"),
    ]

    order_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)
    status = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.ForeignKey(
        Price, on_delete=models.SET_NULL, null=True, blank=True
    )  # 수정: 가격 정보를 참조
    order_price = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # 주문 시점의 가격
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.order_number} ({self.get_order_type_display()}) by {self.customer_name}"

    def save(self, *args, **kwargs):
        # 주문 유형에 따라 상태 선택지를 설정
        if self.order_type == "BUY":
            if self.status not in dict(self.BUY_ORDER_STATUS_CHOICES).keys():
                raise ValueError(f"Invalid status '{self.status}' for a buy order.")
        elif self.order_type == "SELL":
            if self.status not in dict(self.SELL_ORDER_STATUS_CHOICES).keys():
                raise ValueError(f"Invalid status '{self.status}' for a sell order.")

        # Order가 처음 생성될 때만 order_price 설정 및 Invoice 생성
        is_new = self.pk is None  # 새로 생성된 객체인지 확인

        if is_new:
            # 새로운 Order가 생성된 경우, order_price를 현재 가격으로 설정
            if self.price:
                self.order_price = (
                    self.price.price
                )  # 현재 Price 객체의 가격을 order_price에 저장

            # 슈퍼클래스의 save()를 호출하여 데이터베이스에 저장
            super().save(*args, **kwargs)

            # 새로운 Order가 생성된 경우, Invoice 생성
            Invoice.objects.create(
                order=self,
                invoice_number=f"INV{self.order_number}",  # Invoice 번호는 주문 번호를 기반으로 생성
                total_price=self.total_price,
            )
        else:
            # 기존 Order인 경우, 단순히 저장
            super().save(*args, **kwargs)


class Invoice(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="invoice"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    invoice_number = models.CharField(max_length=20, unique=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.invoice_number} for Order {self.order.order_number}"
