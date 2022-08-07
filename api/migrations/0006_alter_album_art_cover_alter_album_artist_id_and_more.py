# Generated by Django 4.1 on 2022-08-07 17:49

import api.helpers.RenameImageToSlug
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_album_created_by_alter_album_updated_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="art_cover",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="JPEG",
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
            name="artist_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="artist_album",
                to="api.artist",
            ),
        ),
        migrations.AlterField(
            model_name="album",
            name="band_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="band_album",
                to="api.band",
            ),
        ),
        migrations.AlterField(
            model_name="artist",
            name="bg_image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="JPEG",
                keep_meta=True,
                max_length=255,
                null=True,
                quality=90,
                scale=None,
                size=[1920, 1080],
                upload_to=api.helpers.RenameImageToSlug.RenameImageToSlug("artist/"),
            ),
        ),
        migrations.AlterField(
            model_name="band",
            name="bg_image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                force_format="JPEG",
                keep_meta=True,
                max_length=255,
                null=True,
                quality=90,
                scale=None,
                size=[1920, 1080],
                upload_to=api.helpers.RenameImageToSlug.RenameImageToSlug("band/"),
            ),
        ),
    ]
