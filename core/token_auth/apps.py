from django.apps import AppConfig


class TokenAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.token_auth'
    verbose_name = 'token_auth'
