from django.db import models
from django.db.models import Model
#from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import json
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSetting(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField(default=10)
    default_game_query = models.CharField(max_length=100, default="")
    #question_types = models.ManyToManyField('QuestionType')
    def __str__(self):
        data = model_to_dict(self)
        return json.dumps(data)

@receiver(post_save, sender=User)
def create_user_setting(sender, instance, created, **kwargs):
    if created:
        UserSetting.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_setting(sender, instance, **kwargs):
    instance.usersetting.save()

#class QuestionType(models.Model):
#    QUESTION_TYPE = (
#        (1, "Find the card out of 4"),
#        (2, "Find the sound out of 4")
#    )
#    type = MultiSelectField(choices=QUESTION_TYPE)
