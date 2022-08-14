from django.db import models
from django.conf import settings

from api.components.album.models import Album


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="genre_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="genre_updated_user")

    def __str__(self) -> str:
        return self.name


class AlbumGenre(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="album_genres")
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_genre_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_genre_updated_user")

    class Meta:
        unique_together = ('album', 'genre')

    def __str__(self) -> str:
        return f"{self.genre}"
