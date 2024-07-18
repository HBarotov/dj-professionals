from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]
    inlines = [
        ReviewInline,
    ]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Book, BookAdmin)
