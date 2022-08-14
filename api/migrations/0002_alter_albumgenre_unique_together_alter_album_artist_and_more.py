# Generated by Django 4.1 on 2022-08-13 22:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="albumgenre",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="api.artist"
            ),
        ),
        migrations.AlterField(
            model_name="album",
            name="band",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to="api.band"
            ),
        ),
        migrations.AlterField(
            model_name="albumgenre",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="album_genres",
                to="api.album",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="albumgenre",
            unique_together={("album", "genre")},
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                ("review_text", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="album_review",
                        to="api.album",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_review",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]