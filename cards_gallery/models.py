from django.db import models
from django_resized import ResizedImageField

class Category(models.Model):
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg',
                              upload_to='category_landscape')
    altText = models.TextField(null=True, blank=True)
    cards = models.ManyToManyField('Card', through='CardItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg',
                              upload_to='category_landscape')
    altText = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CardItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    card = models.ForeignKey('Card', on_delete=models.CASCADE)
