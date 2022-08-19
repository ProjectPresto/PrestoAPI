from django.db import models
from django.conf import settings
from django_resized import ResizedImageField

from api.components.genre.models import Genre

from ...helpers.RenameImageToSlug import RenameImageToSlug
from ..author.models import Artist, Band


class Album(models.Model):
    """
    Modle for the album.
    """
    RELEASE_TYPE_ALBUM_CHOICES = [
        ('LP', 'LP'),
        ('Single', 'Single'),
        ('Compilation', 'Compilation'),
        ('EP', 'EP'),
        ('Live', 'Live Album'),
        ('Remix', 'Remix'),
        ('Soundtrack', 'Soundtrack'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    release_date = models.DateField()
    release_type = models.CharField(
        max_length=11, choices=RELEASE_TYPE_ALBUM_CHOICES, null=False, default="LP")
    artist = models.ForeignKey(
        Artist, on_delete=models.PROTECT, null=True)
    band = models.ForeignKey(
        Band, on_delete=models.PROTECT, null=True)
    art_cover = ResizedImageField(
        size=[720, 720], upload_to=RenameImageToSlug("album/"), max_length=255, null=True)
    art_cover_url = models.URLField(max_length=2048, null=True)
    genres = models.ManyToManyField(Genre, related_name='album_genres')

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_updated_user")

    def __str__(self) -> str:
        if self.band:
            return self.band.name + " - " + self.title
        else:
            return self.artist.name + " - " + self.title
