from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    birth = models.IntegerField()
    death = models.IntegerField()
    movement = models.TextField()
    quotes = models.TextField()

    def __str__(self):
      return self.name
