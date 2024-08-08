from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import (
  CustomUserCreationForm,
  CustomUserChangeForm
)
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
  list_display = [
    "username", "first_name", "last_name", "email", "role", "is_superuser", "is_active", "date_joined"
  ]
  model = CustomUser
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {"fields": ("role",)}),
  )
  fieldsets = UserAdmin.fieldsets + (
    (None, {"fields": ("role",)}),
  )

admin.site.register(CustomUser, CustomUserAdmin)
