from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"  # 모든 필드를 포함
        read_only_fields = [
            "order_id",
            "order_date",
            "created_at",
            "updated_at",
        ]  # 자동 생성 필드
