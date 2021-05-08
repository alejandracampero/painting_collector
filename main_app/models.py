from django.db import models
from django.urls import reverse

class Artist(models.Model):
    name = models.CharField(max_length=100)
    birth = models.IntegerField()
    death = models.IntegerField()
    movement = models.TextField()
    quotes = models.TextField()

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'artist_id': self.id})

class Painting(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    dims = models.TextField()
    location = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
      return self.title