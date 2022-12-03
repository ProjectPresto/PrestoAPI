from django.db import models
from django.conf import settings

from ..album.models import Album
from ..author.models import Artist, Band
from ..track.models import Track

class ServiceLink(models.Model):
    """
    Model for service link.
    """
    SERVICE_CHOICES = [
        ('spotify', 'Spotify'),
        ('apple_music', 'Apple Music'),
        ('tidal', 'Tidal'),
        ('youtube', 'YouTube'),
        ('deezer', 'Deezer'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('bandcamp', 'Bandcamp')
    ]

    link = models.URLField(null=False)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service Link'
        verbose_name_plural = 'Service Links'

class AlbumServiceLink(ServiceLink):
    """
    Model of service link of album.
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album_service_links")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_service_link_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="album_service_link_updated_user")

    class Meta:
        verbose_name = 'Album Service Link'
        verbose_name_plural = 'Album Service Links'

class ArtistServiceLink(ServiceLink):
    """
    Model of service link of album.
    """
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist_service_links")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="artist_service_link_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="artist_service_link_updated_user")

    class Meta:
        verbose_name = 'Artist Service Link'
        verbose_name_plural = 'Artist Service Links'

class BandServiceLink(ServiceLink):
    """
    Model of service link of album.
    """
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="band_service_links")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_service_link_created_user")
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_service_link_updated_user")

    class Meta:
        verbose_name = 'Band Service Link'
        verbose_name_plural = 'Band Service Links'