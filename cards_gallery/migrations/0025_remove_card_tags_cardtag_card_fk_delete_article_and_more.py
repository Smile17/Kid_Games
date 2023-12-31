# Generated by Django 4.2.2 on 2023-07-25 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cards_gallery", "0024_remove_cardtag_card_fk_card_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="tags",
        ),
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
        migrations.DeleteModel(
            name="Article",
        ),
        migrations.DeleteModel(
            name="Publication",
        ),
    ]
