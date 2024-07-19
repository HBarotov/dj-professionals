from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from django.utils.feedgenerator import DefaultFeed

from .models import Book


class CorrectMimeTypeFeed(DefaultFeed):
    content_type = "application/xml; charset=utf-8"


class LatestBooksFeed(Feed):
    feed_type = CorrectMimeTypeFeed
    title = "Bookstore"
    link = reverse_lazy("books:book_list")
    description = "Latest books."

    def items(self):
        return Book.sale.all()[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(item.summary, 30)

    def item_pubdate(self, item):
        return item.updated
