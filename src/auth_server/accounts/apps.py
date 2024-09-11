from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        # 필요한 경우 추가적인 초기화 작업을 여기에 작성합니다.
        pass
