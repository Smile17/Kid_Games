from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField

class Card(models.Model):
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    title = models.CharField(max_length=100)
    image = ResizedImageField(
        size=[1400, 1000],
        crop=["middle", "center"],
        default="default_image.jpg",
        upload_to="image",
    )
    audio = models.FileField(upload_to="audio", default="default_audio.mp3")
    altText = models.TextField(null=True, blank=True)
    cards = models.ManyToManyField('Card', through='CardItem', null=True, blank=True)
    is_category = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CardItem(models.Model):
    parent = models.ForeignKey('Card', on_delete=models.DO_NOTHING, related_name='parent_card', db_column='parent_card',
                               null=True, blank=True)
    child = models.ForeignKey('Card', on_delete=models.DO_NOTHING, related_name='child_card', db_column='child_card',
                              null=True, blank=True)

class CardTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
    tag = models.CharField(max_length=20)


