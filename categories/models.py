from django.db import models

class Category(models.Model):
    category_id = models.IntegerField(unique=True)  # TMDB'den gelen id
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)  # TMDB film ID
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)

    # ManyToManyField ile bir film birden fazla kategoriye ait olabilir
    categories = models.ManyToManyField(Category, related_name="movies")

    def __str__(self):
        return self.title
