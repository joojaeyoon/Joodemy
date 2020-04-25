from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_instructor')
    list_display_links = ('username', 'email')


admin.site.register(User, CustomUserAdmin)
