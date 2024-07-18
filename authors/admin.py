from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "slug"]
    prepopulated_fields = {"slug": ("first_name", "last_name")}
