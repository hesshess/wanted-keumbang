from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("orders.urls")),  # 'orders' 앱 URL 포함
]
