from rest_framework.viewsets import ModelViewSet
from rest_api.models import Album, Artist, Song
from .serializers import ArtistSerializerWeb, AlbumSerializerWeb, SongSerializerWeb


class ArtistAPIWebViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerWeb


class AlbumAPIWebViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializerWeb


class SongAPIWebViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializerWeb
