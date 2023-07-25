# Generated by Django 4.2.2 on 2023-07-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0029_remove_book_authors_delete_author_delete_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cardtag1",
            name="user",
        ),
        migrations.RemoveField(
            model_name="cardtag",
            name="card_fk",
        ),
        migrations.AddField(
            model_name="card",
            name="tags",
            field=models.ManyToManyField(
                related_name="tags", to="cards_gallery.cardtag"
            ),
        ),
        migrations.DeleteModel(
            name="Card1",
        ),
        migrations.DeleteModel(
            name="CardTag1",
        ),
    ]
