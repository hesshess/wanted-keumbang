from django.db import models


class Product(models.Model):
    """
    상품을 정의하는 모델입니다.
    """

    product_id = models.AutoField(primary_key=True)  # 상품 고유 식별자 (자동 증가)
    product_name = models.CharField(max_length=255)  # 상품명 (예: 99.9% 금, 99.99% 금)
    price = models.ForeignKey(
        "Price", on_delete=models.SET_NULL, null=True, blank=True
    )  # 현재 적용된 가격의 외래 키
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.product_name


class Price(models.Model):
    """
    상품의 가격 변동을 관리하는 모델입니다.
    """

    price_id = models.AutoField(primary_key=True)  # 가격 고유 식별자 (자동 증가)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )  # 가격이 적용되는 상품 외래 키
    price_per_gram = models.DecimalField(max_digits=10, decimal_places=2)  # 그램당 가격
    effective_date = models.DateField()  # 가격이 적용된 날짜
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return f"{self.product.product_name} - {self.price_per_gram} per gram (Effective from {self.effective_date})"
