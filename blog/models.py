from django.db import models

# Create your models here.
# class Post(models.Model):
#     title = models
from django.utils import timezone

topic =(
    ('new','NEW'),
    ('trending','TRENDING'),
    ('hot','HOT')
    )

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    jdate = models.DateTimeField(default=timezone.now)
    topic = models.CharField(choices=topic, default='new', max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title