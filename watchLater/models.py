from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WatchLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id= models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)



class Meta:
        unique_together = ('user', 'movie_id')  # aynı kullanıcı aynı filmi iki kez eklemesin


