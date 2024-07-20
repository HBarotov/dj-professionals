from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Profile

CustomUser = get_user_model()


class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "city", "region", "country"]
    raw_id_fields = ["user"]


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = list_display = ["username", "email", "is_superuser"]
    inlines = [ProfileInline]


admin.site.register(CustomUser, CustomUserAdmin)
