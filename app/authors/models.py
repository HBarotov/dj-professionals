import os

from django.db import models
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
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)

        if self.profile and self.profile.name != "author.png":
            ext = self.profile.name.split(".")[-1]
            new_filename = f"authors/{self.slug}.{ext}"
            self.profile.storage.delete(new_filename)  # Ensure no file conflicts
            self.profile.storage.save(new_filename, self.profile.file)
            self.profile.name = new_filename

            super().save(update_fields=["profile"])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
