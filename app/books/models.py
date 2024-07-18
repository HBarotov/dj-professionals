from authors.models import Author
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    authors = models.ManyToManyField(Author, related_name="books_written")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.PositiveIntegerField(default=2024)
    edition = models.PositiveSmallIntegerField(default=1)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book_detail", args=[str(self.id), self.slug])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.author} - {self.review}"
