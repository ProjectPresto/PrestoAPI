# Generated by Django 4.1.1 on 2022-12-03 21:33

import api.helpers.RenameImageToSlug
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_alter_track_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="art_cover",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format="WebP",
                keep_meta=True,
                max_length=255,
                null=True,
                quality=90,
                scale=None,
                size=[720, 720],
                upload_to=api.helpers.RenameImageToSlug.RenameImageToSlug("album/"),
            ),
        ),
        migrations.AlterField(
            model_name="album",
            name="art_cover_url",
            field=models.URLField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name="album",
            name="genres",
            field=models.ManyToManyField(
                blank=True, related_name="album_genres", to="api.genre"
            ),
        ),
    ]
