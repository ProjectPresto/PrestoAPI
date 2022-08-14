from django.db import models
from django.conf import settings

from ..album.models import Album
from ..author.models import Artist, Band


class Track(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=False, related_name="tracks")
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


class FeaturedAuthor(models.Model):
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, null=False, related_name="featured_authors")
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="featured_author_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="featured_author_updated_user")
