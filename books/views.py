from django.contrib.auth import mixins
from django.views import generic

from .models import Book


class BookListView(mixins.LoginRequiredMixin, generic.ListView):
    queryset = Book.objects.order_by("-pk")
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"


class BookDetailView(
    mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic.DetailView
):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"
