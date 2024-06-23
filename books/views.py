from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    queryset = Book.objects.order_by("-pk")
    template_name = "books/book_list.html"
    context_object_name = "book_list"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
