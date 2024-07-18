from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "pages/home.html"


class AboutPageView(generic.TemplateView):
    template_name = "pages/about.html"


class ContactPageView(generic.TemplateView):
    template_name = "pages/contact.html"
