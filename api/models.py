import os
from time import timezone
from django.db import models
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from uuid import uuid4


@deconstructible
class RenameImageToSlug(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if instance.slug:
            filename = '{}.{}'.format(instance.slug, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


class Album(models.Model):
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
    # artist_id = models.ForeignKey()
    # band_id = models.ForeignKey()
    art_cover = ResizedImageField(
        size=[720, 720], upload_to=RenameImageToSlug("album/art_covers/"), max_length=255)
    art_cover_url = models.URLField(max_length=2048)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
