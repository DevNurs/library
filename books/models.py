from django.db import models
from django.utils import timezone


class Books(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.DateField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        

