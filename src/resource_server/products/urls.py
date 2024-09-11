from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PriceViewSet

router = DefaultRouter()
router.register(r"prices", PriceViewSet)
router.register(r"", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
