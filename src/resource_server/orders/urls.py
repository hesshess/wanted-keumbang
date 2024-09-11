from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet)
router.register(r"invoices", InvoiceViewSet)  # 인보이스 URL 라우팅 추가

urlpatterns = [
    path("", include(router.urls)),
]
