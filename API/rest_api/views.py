from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Album, Artist, Song
from .serializers import ArtistSerializerTelegram, AlbumSerializerTelegram, SongSerializerTelegram


class ArtistAPITelegramViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerTelegram


class AlbumAPITelegramViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializerTelegram


class SongAPITelegramViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializerTelegram
