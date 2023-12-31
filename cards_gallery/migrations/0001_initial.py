# Generated by Django 4.2.2 on 2023-07-01 16:27

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=["middle", "center"],
                        default="default_land.jpg",
                        force_format=None,
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[2878, 1618],
                        upload_to="category_landscape",
                    ),
                ),
                ("altText", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
