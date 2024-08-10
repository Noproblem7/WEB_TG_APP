from django.contrib import admin
from django.urls import path, include
from .views import HomeView, AlbumView, ArtistView, SongView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('album/', AlbumView.as_view(), name='albom'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('song/', SongView.as_view(), name='song'),
]
