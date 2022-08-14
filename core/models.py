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
            # Generate a unique slug
            count = 0
            while True:
                slug = slugify(self.username)
                if count > 0:
                    slug = f"{slug}-{count}"
                if not User.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break
                count += 1
        return super().save(*args, **kwargs)
