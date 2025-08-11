from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FavotiteMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movieId = models.IntegerField()
    title = models.CharField(max_length=1000)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.movieId})"

