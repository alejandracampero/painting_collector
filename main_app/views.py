from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Artist
from .forms import PaintingForm

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
  painting_form = PaintingForm()
  return render(request, 'artists/detail.html', { 'artist': artist, 'painting_form': painting_form })

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

def add_painting(request, artist_id):
  # create a ModelForm instance using the data in request.POST
  form = PaintingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the artist_id assigned
    new_painting = form.save(commit=False)
    new_painting.artist_id = artist_id
    new_painting.save()
  return redirect('detail', artist_id=artist_id)