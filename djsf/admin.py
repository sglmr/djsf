from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUser

# Register the custom user model
admin.site.register(AppUser, UserAdmin)
