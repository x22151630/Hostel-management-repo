from django.db import models

# Create your models here.
class HostelManagement(models.Model):

    title = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    release_date = models.DateTimeField('release date')
    genre = models.CharField(max_length=200)
    duration = models.FloatField()
