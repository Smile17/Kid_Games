# Generated by Django 4.2.2 on 2023-07-25 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0026_card_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="tags",
        ),
    ]
