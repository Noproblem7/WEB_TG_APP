from .models import Artist, Album, Song
from rest_framework import serializers


class ArtistSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name')


class AlbumSerializerTelegram(serializers.ModelSerializer):
    artist = ArtistSerializerTelegram()

    class Meta:
        model = Album
        fields = ('title', 'artist')


class SongSerializerTelegram(serializers.ModelSerializer):
    album = AlbumSerializerTelegram()

    class Meta:
        model = Song
        fields = ('title', 'image', 'album')
