# Generated by Django 4.2.2 on 2023-07-30 16:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0030_remove_cardtag1_user_remove_cardtag_card_fk_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="altText",
        ),
    ]
