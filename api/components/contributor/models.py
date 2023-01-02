from django.conf import settings
from django.db import models
from django_resized import ResizedImageField

from api.helpers.rename_image_to_slug import RenameImageToSlug


class Contributor(models.Model):
    """ 
    Model for the contributor.
    Contributor is a user extended by the fields related to user profile.
    Also serializer containes fields like count of contributions or ratings.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributor')
    about_text = models.TextField(null=True, blank=True)
    profile_picture = ResizedImageField(
        size=[500, 500], upload_to=RenameImageToSlug("profile_picture/"), max_length=255, null=True)
    profile_picture_url = models.URLField(max_length=2048, null=True)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"
