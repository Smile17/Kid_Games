"""
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import json


class GameHeader(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField(default=10)
    questions = models.OneToManyField('GameQuestion', on_delete=models.CASCADE)
    def __str__(self):
        data = model_to_dict(self)
        return json.dumps(data)

FIND_PICTURE = 'Find picture'
FIND_SOUND = 'Find sound'

CHOICES_QUESTION_TYPE = (
    (FIND_PICTURE, FIND_PICTURE),
    (FIND_SOUND, FIND_SOUND),
)

class GameQuestion(models.Model):
    game = models.ForeignKey('GameHeader', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=255, choices=CHOICES_QUESTION_TYPE, default=FIND_PICTURE)
    question_data = models.TextField()
    answer_data = models.TextField()
    is_correct = models.BooleanField()

"""