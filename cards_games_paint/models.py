from django.db import models


class PaintImageFile(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField()
    canvas_image = models.TextField()

    def __unicode__(self):
        return self.name