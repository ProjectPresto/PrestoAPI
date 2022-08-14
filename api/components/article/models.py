from django.db import models
from django.conf import settings

from ..album.models import Album
from ..author.models import Artist, Band
from ..track.models import Track


class Article(models.Model):
    """
    Model for articles.
    """
    article_text = models.TextField()
    source = models.CharField(max_length=255, null=True)
    source_url = models.URLField(max_length=2048, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class AlbumArticle(Article):
    """
    Model for album articles.
    """
    album = models.OneToOneField(Album, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_article_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_article_updated_user")

    class Meta:
        verbose_name = 'Album Article'
        verbose_name_plural = 'Album Articles'


class ArtistArticle(Article):
    """
    Model for artist articles.
    """
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="artist_article_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="artist_article_updated_user")

    class Meta:
        verbose_name = 'Artist Article'
        verbose_name_plural = 'Artist Articles'


class BandArticle(Article):
    """
    Model for band articles.
    """
    band = models.OneToOneField(Band, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_article_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_article_updated_user")

    class Meta:
        verbose_name = 'Band Article'
        verbose_name_plural = 'Band Articles'


class TrackArticle(Article):
    """
    Model for track articles.
    """
    track = models.OneToOneField(Track, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="track_article_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="track_article_updated_user")

    class Meta:
        verbose_name = 'Track Article'
        verbose_name_plural = 'Track Articles'
