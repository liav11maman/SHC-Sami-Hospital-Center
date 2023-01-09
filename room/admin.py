from django.contrib import admin

# Register your models here.

from .models import Room, Message
import base.admin

admin.site.register(Room)
admin.site.register(Message)
