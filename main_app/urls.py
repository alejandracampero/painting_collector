from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('artists/', views.artists_index, name='index'),
  path('artists/<int:artist_id>/', views.artists_detail, name='detail'),
  path('artists/create/', views.ArtistCreate.as_view(), name='artists_create'),
  path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artists_update'),
  path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artists_delete'),
  path('artists/<int:artist_id>/add_painting/', views.add_painting, name='add_painting'),
  path('art/<int:pk>/', views.ArtDetail.as_view(), name='art_detail'),
  path('art/create/', views.ArtCreate.as_view(), name='art_create'),
  path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='art_update'),
  path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='art_delete'),
  path('art/', views.ArtList.as_view(), name='art_index'),
  path('artists/<int:artist_id>/assoc_art/<int:art_id>/', views.assoc_art, name='assoc_art'),
  path('artists/<int:artist_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accounts/signup/', views.signup, name='signup'),
]