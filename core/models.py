from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify


class User(AbstractUser):
    email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True, null=False)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
