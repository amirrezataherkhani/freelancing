from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User, Profile


# ordering is commented on UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "is_active", "is_staff")


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Profile)
