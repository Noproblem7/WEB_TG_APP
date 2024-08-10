from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()


class Album(models.Model):
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    image = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.title

class SongAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song)