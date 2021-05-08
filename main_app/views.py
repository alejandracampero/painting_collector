from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Artist

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def artists_index(request):
  artists = Artist.objects.all()
  return render(request, 'artists/index.html', { 'artists': artists })

def artists_detail(request, artist_id):
  artist = Artist.objects.get(id=artist_id)
  return render(request, 'artists/detail.html', { 'artist': artist })

class ArtistCreate(CreateView):
  model = Artist
  fields = ['name', 'birth', 'death', 'movement', 'quotes']
  success_url = '/artists/'