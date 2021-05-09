from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from .models import Artist, Photo
from .forms import PaintingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'art-collector'

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def artists_index(request):
  artists = Artist.objects.filter(user=request.user)
  return render(request, 'artists/index.html', { 'artists': artists })

@login_required
def artists_detail(request, artist_id):
  artist = Artist.objects.get(id=artist_id)
  painting_form = PaintingForm()
  return render(request, 'artists/detail.html', { 'artist': artist, 'painting_form': painting_form })

class ArtistCreate(LoginRequiredMixin, CreateView):
  model = Artist
  fields = ['name', 'birth', 'death', 'movement', 'quotes']
  success_url = '/artists/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user 
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class ArtistUpdate(LoginRequiredMixin, UpdateView):
  model = Artist
  # Let's disallow the renaming of a artist by excluding the name field!
  fields = ['name', 'birth', 'death', 'movement', 'quotes']

class ArtistDelete(LoginRequiredMixin, DeleteView):
  model = Artist
  success_url = '/artists/'

@login_required
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

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
