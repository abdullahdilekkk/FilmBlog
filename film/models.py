from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField()