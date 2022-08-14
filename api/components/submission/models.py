from django.db import models


class EditSubmission(models.Model):
    """
    Model for edit submissions. 
    """
    TABLES = (
        ('album', 'Album'),
        ('artist', 'Artist'),
        ('band', 'Band'),
        ('track', 'Track'),
        ('albumgenre', 'Album Genre'),
        ('genre', 'Genre'),
        ('featuredauthor', 'Featured Author'),
    )
    table = models.CharField(max_length=255, choices=TABLES)
    column = models.CharField(max_length=255)
    object_id = models.IntegerField()
    old_value = models.JSONField()
    new_value = models.JSONField()
    # old_article =
