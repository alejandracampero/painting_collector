from django.contrib import admin
from .models import Artist, Painting, Art, Photo

# Register your models here.
admin.site.register(Artist)
admin.site.register(Painting)
admin.site.register(Art)
admin.site.register(Photo)