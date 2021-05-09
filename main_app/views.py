from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from .models import Artist, Photo
from .forms import PaintingForm

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'art-collector'

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

def add_photo(request, painting_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to painting_id or painting (if you have a painting object)
      photo = Photo(url=url, painting_id=painting_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', painting_id=painting_id)