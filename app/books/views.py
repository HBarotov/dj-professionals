from django.contrib.auth import mixins
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import F, Value
from django.db.models.functions import Concat, Greatest
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import ReviewForm
from .models import Book


class BookListView(ListView):
    queryset = Book.sale.order_by("-pk")
    template_name = "books/list.html"
    context_object_name = "books"
    login_url = "account_login"
    paginate_by = 10


class ReviewGet(DetailView):
    model = Book
    template_name = "books/detail.html"
    context_object_name = "book"
    queryset = Book.sale.all().prefetch_related(
        "reviews__author",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm
        return context


class ReviewPost(mixins.LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Book
    form_class = ReviewForm
    template_name = "books/detail.html"
    context_object_name = "book"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.object
        review.author = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("books:book_detail", args=[self.object.pk, self.object.slug])


class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)


class SearchResultsListView(ListView):
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
