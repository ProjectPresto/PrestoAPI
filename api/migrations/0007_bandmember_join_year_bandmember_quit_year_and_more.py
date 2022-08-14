# Generated by Django 4.1 on 2022-08-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_bandmember"),
    ]

    operations = [
        migrations.AddField(
            model_name="bandmember",
            name="join_year",
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name="bandmember",
            name="quit_year",
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="bandmember",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="bandmember",
            name="roles",
            field=models.CharField(max_length=255, null=True),
        ),
    ]