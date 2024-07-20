from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = CountryField()

    def __str__(self):
        return f"Profile of {self.user.username}"
