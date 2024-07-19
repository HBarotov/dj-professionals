from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "year", "copy", "available"]
    list_filter = ["price", "authors", "available", "year"]
    inlines = [
        ReviewInline,
    ]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["available"]


admin.site.register(Book, BookAdmin)
