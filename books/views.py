from django.contrib.auth import mixins
from django.db.models import Q
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
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )


class SearchResultsListView(generic.ListView):
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains="api")
        )
