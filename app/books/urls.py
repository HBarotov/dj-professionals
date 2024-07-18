from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("search/", views.SearchResultsListView.as_view(), name="search_results"),
    path("<uuid:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("", views.BookListView.as_view(), name="book_list"),
]
