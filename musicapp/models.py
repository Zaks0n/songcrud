from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    likes = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.lyric
