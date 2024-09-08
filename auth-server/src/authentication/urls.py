from django.urls import path
from .views import ObtainTokenView

urlpatterns = [
    path("token/", ObtainTokenView.as_view(), name="token_obtain"),
]
