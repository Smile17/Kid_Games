from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from django.db.models import CharField
from django.db.models.functions import Length

CharField.register_lookup(Length, 'length')


class CardTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.CharField(max_length=20)

    #class Meta:
    #    unique_together = ('user', 'tag',)

    def __str__(self):
        return self.tag + " " + str(self.user)

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
    cards = models.ManyToManyField('Card', through='CardItem', null=True, blank=True)
    tags = models.ManyToManyField(CardTag, related_name='tags', null=True, blank=True)
    is_category = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class CardItem(models.Model):
    parent = models.ForeignKey('Card', on_delete=models.DO_NOTHING, related_name='parent_card', db_column='parent_card',
                               null=True, blank=True)
    child = models.ForeignKey('Card', on_delete=models.DO_NOTHING, related_name='child_card', db_column='child_card',
                              null=True, blank=True)








