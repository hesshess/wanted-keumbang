from rest_framework import serializers
from .models import Order, Invoice

from products.models import Product, Price


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    price = serializers.PrimaryKeyRelatedField(
        queryset=Price.objects.all(), allow_null=True
    )

    class Meta:
        model = Order
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"
