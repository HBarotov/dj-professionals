from django.test import SimpleTestCase
from django.urls import resolve, reverse

from . import views


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_home_page_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, views.HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:about")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "pages/about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "about page")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_about_page_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, views.AboutPageView.as_view().__name__)


class ContactPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:contact")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_page_template(self):
        self.assertTemplateUsed(self.response, "pages/contact.html")

    def test_contact_page_contains_correct_html(self):
        self.assertContains(self.response, "contact page")

    def test_contact_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_contact_page_url_resolves_contactpageview(self):
        view = resolve("/contact/")
        self.assertEqual(view.func.__name__, views.ContactPageView.as_view().__name__)


class Custom404Tests(SimpleTestCase):
    def setUp(self):
        url = "/404/does/not/exist"
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 404)

    def test_404_page_template(self):
        self.assertTemplateUsed(self.response, "404.html")
