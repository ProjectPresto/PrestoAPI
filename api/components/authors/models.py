from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from ...helpers.RenameImageToSlug import RenameImageToSlug


class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    bg_image = ResizedImageField(
        upload_to=RenameImageToSlug("artist/"), max_length=255, null=True)
    bg_image_url = models.URLField(max_length=2048, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="artist_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="artist_updated_user")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Band(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    founding_year = models.IntegerField(null=True)
    breakup_year = models.IntegerField(null=True)
    bg_image = ResizedImageField(
        upload_to=RenameImageToSlug("band/"), max_length=255, null=True)
    bg_image_url = models.URLField(max_length=2048, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_updated_user")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
