from django.db import models
from django.db.models import Model
#from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from cards_games.models import GameType


class UserSetting(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField(default=10)
    default_game_query = models.CharField(max_length=100, default="")
    games = models.ManyToManyField(GameType, related_name='games')
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_setting(sender, instance, created, **kwargs):
    if created:
        UserSetting.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_setting(sender, instance, **kwargs):
    instance.usersetting.save()

