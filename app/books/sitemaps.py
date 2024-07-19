from django.contrib.sitemaps import Sitemap

from .models import Book


class BookSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Book.sale.all()

    def lastmod(self, obj):
        return obj.updated
