from django.apps import AppConfig
from django.core.signals import request_finished


class ChatBotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chat_bot"

    def ready(self):
        from . import signals

        request_finished.connect(signals.on_pragma_save)