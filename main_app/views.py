from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class ArtistUpdate(UpdateView):
  model = Artist
  # Let's disallow the renaming of a artist by excluding the name field!
  fields = ['name', 'birth', 'death', 'movement', 'quotes']

class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/artists/'