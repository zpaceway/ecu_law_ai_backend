from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from chat_bot.models import Pragma
from chat_bot import chat_bot_index


@receiver(post_save, sender=Pragma)
def on_pragma_save(sender, instance: Pragma = None, **kwargs):
    if not instance:
        return

    chat_bot_index.refresh_model()


@receiver(pre_delete, sender=Pragma)
def on_pragma_delete(sender, instance: Pragma = None, **kwargs):
    if not instance:
        return

    instance.file.delete()
    chat_bot_index.refresh_model()
