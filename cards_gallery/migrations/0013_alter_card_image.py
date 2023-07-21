# Generated by Django 4.2.2 on 2023-07-17 07:26

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0012_alter_card_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=["middle", "center"],
                default="default_image.jpg",
                force_format=None,
                keep_meta=True,
                quality=75,
                scale=None,
                size=[1000, 1000],
                upload_to="image",
            ),
        ),
    ]