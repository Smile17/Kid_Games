# Generated by Django 4.2.2 on 2023-07-25 20:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0028_author_cardtag1_card1_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="authors",
        ),
        migrations.DeleteModel(
            name="Author",
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]
