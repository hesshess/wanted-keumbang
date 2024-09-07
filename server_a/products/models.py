from django.db import models


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("999", "99.9% 금"),
        ("9999", "99.99% 금"),
    ]

    product_id = models.AutoField(primary_key=True)  # 상품 ID
    product_name = models.CharField(
        max_length=20, choices=PRODUCT_TYPE_CHOICES, unique=True
    )  # 상품명
    description = models.TextField(blank=True, null=True)  # 상품 설명 (선택 사항)

    def __str__(self):
        return self.product_name
