from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Author


class AuthorDetailView(DetailView):
    model = Author
    template_name = "authors/detail.html"
    context_object_name = "author"

    def get_queryset(self):
        qs = Author.objects.prefetch_related("books_written")
        return qs


class AuthorListView(ListView):
    model = Author
    template_name = "authors/list.html"
    context_object_name = "authors"
    paginate_by = 10

    def get_queryset(self):
        qs = (
            Author.objects.prefetch_related("books_written")
            .annotate(book_count=Count("books_written"))
            .order_by("-book_count")
        )
        return qs
