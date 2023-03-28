from django.contrib.auth.models import User, Group
from django.contrib import admin
from chat_bot.models import Pragma


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Pragma)
