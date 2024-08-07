from django.contrib import admin
from .models import CustomUser, Item, Status


admin.site.register(CustomUser)
admin.site.register(Item)
admin.site.register(Status)