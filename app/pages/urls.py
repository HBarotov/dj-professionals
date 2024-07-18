from django.urls import path

from . import views

app_name = "pages"
urlpatterns = [
    path("contact/", views.ContactPageView.as_view(), name="contact"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("", views.HomePageView.as_view(), name="home"),
]
