from django.apps import AppConfig
from django_rest_passwordreset.signals import reset_password_token_created


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
            from .emails import send_password_reset_email

            reset_password_token_created.connect(send_password_reset_email)