# Generated by Django 4.2.2 on 2023-08-02 13:57

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameType",
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
                ("title", models.CharField(max_length=50, unique=True)),
                ("description", models.CharField(max_length=100)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=["middle", "center"],
                        default="default_image.jpg",
                        force_format=None,
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[1400, 1000],
                        upload_to="image",
                    ),
                ),
            ],
        ),
    ]
