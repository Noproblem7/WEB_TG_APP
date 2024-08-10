from rest_api.models import Artist, Album, Song
from rest_framework import serializers


class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'username')


class AlbumSerializerWeb(serializers.ModelSerializer):
    artist = ArtistSerializerWeb()

    class Meta:
        model = Album
        fields = ('title', 'artist')


class SongSerializerWeb(serializers.ModelSerializer):
    album = AlbumSerializerWeb()

    class Meta:
        model = Song
        fields = ('title', 'image', 'album')
