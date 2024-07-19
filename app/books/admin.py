from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["review", "author", "book", "active"]
    list_filter = ["book", "author", "active"]
    date_hierarchy = "created"
    raw_id_fields = ["book", "author"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "year", "copy", "available"]
    list_filter = ["price", "authors", "available", "year"]
    inlines = [
        ReviewInline,
    ]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["available"]
    ordering = ["price", "year"]


admin.site.register(Book, BookAdmin)
