from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPES = (
    ('P', 'Painting'),
    ('S', 'Sculpture'),
    ('D', 'Drawing')
)

class Art(models.Model):
  title = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  description = models.TextField(max_length=700)
  dims = models.TextField()
  location = models.TextField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('art_detail', kwargs={'pk': self.id})

class Artist(models.Model):
    name = models.CharField(max_length=100)
    birth = models.IntegerField()
    death = models.IntegerField()
    movement = models.TextField()
    quotes = models.TextField()
    art = models.ManyToManyField(Art)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.name
    
    class Meta:
      ordering = ['name']

    def get_absolute_url(self):
      return reverse('detail', kwargs={'artist_id': self.id})

class Type(models.Model):
    type = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TYPES,
    # set the default value for Type to be 'P'
    default=TYPES[0][0]
  )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
          return f"{self.get_type_display()}"


class Photo(models.Model):
  url = models.CharField(max_length=200)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for artist_id: {self.artist_id} @{self.url}"