from django.contrib import admin
from .models import UserAuthentication, Post, Message,ChatRoom
# Register your models here.

admin.site.register(UserAuthentication)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(ChatRoom)