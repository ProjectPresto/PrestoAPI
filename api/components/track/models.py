from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

from ..album.models import Album


class Track(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    album_id = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=False, related_name="album_track")
    position = models.PositiveIntegerField(null=True)
    duration = models.DurationField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="track_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="track_updated_user")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
