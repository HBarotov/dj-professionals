from django.urls import path

from . import views

app_name = "authors"
urlpatterns = [
    path(
        "<int:pk>/<slug:slug>/", views.AuthorDetailView.as_view(), name="author_detail"
    ),
    path("", views.AuthorListView.as_view(), name="author_list"),
]
