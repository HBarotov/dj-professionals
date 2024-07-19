from authors.models import Author
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(copy__gt=0)


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255)
    summary = models.TextField()
    slug = models.SlugField(unique=True, max_length=200)
    authors = models.ManyToManyField(Author, related_name="books_written")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    year = models.PositiveIntegerField(default=2024)
    cover = models.ImageField(upload_to="covers/", blank=True)
    copy = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # The default manager
    sale = AvailableManager()  # Our custom manager.

    class Meta:
        indexes = [
            models.Index(fields=["copy"], name="copy_index"),
        ]
        ordering = ["-pk"]
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.copy > 0:
            self.available = True
        else:
            self.available = False
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("books:book_detail", args=[str(self.id), self.slug])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="reviews"
    )
    review = models.CharField(max_length=255)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"{self.author} - {self.review}"
