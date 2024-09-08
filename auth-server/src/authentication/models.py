from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass  # 필요에 따라 사용자 모델 확장
