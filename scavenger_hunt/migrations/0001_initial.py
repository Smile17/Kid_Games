# Generated by Django 4.2.2 on 2023-07-16 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cards_gallery", "0009_delete_scavengercardtest"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScavengerCard",
            fields=[
                (
                    "card",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="cards_gallery.card",
                    ),
                ),
            ],
        ),
    ]
