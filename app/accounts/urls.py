from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("edit/", views.edit, name="edit"),
    path("profile/", views.profile, name="profile"),
]
