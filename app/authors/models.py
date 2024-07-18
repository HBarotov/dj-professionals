import os

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def author_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.slug}.{ext}"
    return os.path.join("authors/", filename)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    email = models.EmailField(blank=True)
    profile = models.ImageField(upload_to=author_image_upload_to, default="author.png")

    def save(self, *args, **kwargs):
        # Generate the slug from the first name and last name
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)  # Save the instance to generate the ID

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("authors:author_detail", args=[self.pk, self.slug])
