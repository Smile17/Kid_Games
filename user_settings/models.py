from django.db import models
from django.db.models import Model


class UserSettingsModel(Model):
    with_sounds = models.BinaryField()
