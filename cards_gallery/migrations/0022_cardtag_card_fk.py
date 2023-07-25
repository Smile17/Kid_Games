# Generated by Django 4.2.2 on 2023-07-25 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0021_remove_card_tags_remove_cardtag_card_pk"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardtag",
            name="card_fk",
            field=models.ForeignKey(
                blank=True,
                db_column="card_fk",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="card_fk",
                to="cards_gallery.card",
            ),
        ),
    ]
