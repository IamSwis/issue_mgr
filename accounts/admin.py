from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ( 
    CustomUserCreationForm, 
    CustomUserChangeForm
)
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "role",
        "team",
    ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("None", {"fields": ("role", "team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ("None", {"fields": ("role", "team")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
