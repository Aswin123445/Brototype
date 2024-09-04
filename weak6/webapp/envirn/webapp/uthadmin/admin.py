from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import AswinUser

class CustomUserAdmin(UserAdmin):
    model = AswinUser
    list_display = ['email', 'username',]

admin.site.register(AswinUser, CustomUserAdmin)