from rest_framework import viewsets
from .models import Product, Price
from .serializers import ProductSerializer, PriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product의 CRUD 작업을 위한 ViewSet
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PriceViewSet(viewsets.ModelViewSet):
    """
    Price의 CRUD 작업을 위한 ViewSet
    """

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
