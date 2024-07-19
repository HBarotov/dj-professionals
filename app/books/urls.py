from django.urls import path

from . import views
from .feeds import LatestBooksFeed

app_name = "books"
urlpatterns = [
    path("search/", views.SearchResultsListView.as_view(), name="search_results"),
    path("<int:pk>/<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),
    path("feed/", LatestBooksFeed(), name="book_feed"),
    path("", views.BookListView.as_view(), name="book_list"),
]
