# Generated by Django 4.2.2 on 2023-07-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_settings", "0002_rename_with_autoplay_usersettings_autoplay_sound"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersettings",
            name="number_of_questions",
            field=models.PositiveIntegerField(default=10),
        ),
    ]
