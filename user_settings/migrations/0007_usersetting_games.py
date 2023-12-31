# Generated by Django 4.2.2 on 2023-08-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cards_games", "0003_alter_gametype_description"),
        ("user_settings", "0006_usersetting_default_game_query"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersetting",
            name="games",
            field=models.ManyToManyField(
                related_name="games", to="cards_games.gametype"
            ),
        ),
    ]
