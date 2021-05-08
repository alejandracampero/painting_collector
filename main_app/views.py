from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Artist:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, birth, death, movement, quotes):
    self.name = name
    self.birth = birth
    self.death = death
    self.movement = movement
    self.quotes = quotes

def artists_index(request):
 return render(request, 'artists/index.html', { 'artists': artists })
