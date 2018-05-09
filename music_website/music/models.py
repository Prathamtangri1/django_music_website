from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length=20)
    title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
