# Generated by Django 4.1 on 2022-08-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_bandmember_join_year_bandmember_quit_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandmember",
            name="join_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="bandmember",
            name="quit_year",
            field=models.IntegerField(null=True),
        ),
    ]