from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from ..album.models import Album


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name="user_review")
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=False, related_name="album_review")
    rating = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.album} ({self.rating})"
