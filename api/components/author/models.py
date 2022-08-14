from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from ...helpers.RenameImageToSlug import RenameImageToSlug


class Artist(models.Model):
    """
    Model for the artist.
    Artist is a one person who creates albums, can write and produce albums.
    Artist is not a group of people.
    """
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


class Band(models.Model):
    """
    Model for the band.
    Band is a group of artists who create albums, can write and produce albums.
    Band member can be an artist or a not specified artist. More in BandMember model
    """
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


class BandMember(models.Model):
    """
    Model for the band member.
    Band member is a person who is member of the band.
    Band member can be an artist or a not specified before in database person.
    """
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    roles = models.CharField(max_length=255, null=True)
    join_year = models.IntegerField(null=True)
    quit_year = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_member_created_user")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="band_member_updated_user")

    def __str__(self) -> str:
        if self.artist:
            return f"{self.band.name} - {self.artist.name}"
        else:
            return f"{self.band.name} - {self.name}"
