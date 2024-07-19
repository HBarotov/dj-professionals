from django.contrib.auth import mixins
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import F, Value
from django.db.models.functions import Concat, Greatest
from django.views import generic

from .models import Book


class BookListView(mixins.LoginRequiredMixin, generic.ListView):
    queryset = Book.sale.order_by("-pk")
    template_name = "books/list.html"
    context_object_name = "books"
    login_url = "account_login"
    paginate_by = 10


class BookDetailView(
    mixins.LoginRequiredMixin, mixins.PermissionRequiredMixin, generic.DetailView
):
    model = Book
    template_name = "books/detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.sale.all().prefetch_related(
        "reviews__author",
    )


class SearchResultsListView(generic.ListView):
    context_object_name = "books"
    template_name = "books/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = (
            Book.sale.annotate(
                title_similarity=TrigramSimilarity("title", query),
                author_similarity=TrigramSimilarity(
                    Concat(
                        F("authors__first_name"), Value(" "), F("authors__last_name")
                    ),
                    query,
                ),
            )
            .annotate(similarity=Greatest("title_similarity", "author_similarity"))
            .filter(similarity__gt=0.1)
            .order_by("-similarity")
        ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context["query"] = query
        return context
