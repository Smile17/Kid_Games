from django.db import models
from cards_gallery.models import Card

class ScavengerCard(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE, primary_key=True)


