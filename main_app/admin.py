from django.contrib import admin
from .models import Artist, Type, Art, Photo

# Register your models here.
admin.site.register(Artist)
admin.site.register(Type)
admin.site.register(Art)
admin.site.register(Photo)