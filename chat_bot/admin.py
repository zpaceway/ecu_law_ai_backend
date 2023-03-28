from django.contrib.auth.models import User, Group
from django.contrib import admin
from chat_bot.models import Pragma
from chat_bot import chat_bot_index

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Pragma)

admin.site.add_action(chat_bot_index.refresh_model, "Refresh Model")
