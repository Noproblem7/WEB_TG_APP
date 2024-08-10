from django.shortcuts import render
from django.views import View
import requests

class HomeView(View):
    def get(self, request):
        artist = requests.get("http://127.0.0.1:8000/web_app/artistweb/").json()
        context = {
            'artist': artist
        }
        return render(request, 'home.html', context)


class ArtistView(View):
    def get(self, request):
        artist = requests.get("http://127.0.0.1:8000/web_app/artistweb/").json()
        context = {
            'artist': artist
        }
        return render(request, 'artist.html', context)


class AlbumView(View):
    def get(self, request):
        alboms = requests.get("http://127.0.0.1:8000/web_app/albumweb/").json()
        context = {
            'alboms': alboms
        }
        return render(request, 'albom.html', context)


class SongView(View):
    def get(self, request):
        songs = requests.get("http://127.0.0.1:8000/web_app/songweb/").json()
        context = {
            'songs': songs
        }
        return render(request, 'song.html', context)

