# Generated by Django 4.1.1 on 2022-12-03 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_servicelink_bandservicelink_artistservicelink_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="albumservicelink",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="album_service_links",
                to="api.album",
            ),
        ),
        migrations.AlterField(
            model_name="artistservicelink",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="artist_service_links",
                to="api.artist",
            ),
        ),
        migrations.AlterField(
            model_name="bandservicelink",
            name="band",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="band_service_links",
                to="api.band",
            ),
        ),
    ]