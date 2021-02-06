from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    year = models.IntegerField(default=2000)
    director =  models.CharField(default="awaiting director", max_length=80)
    genre = models.CharField(default="awaiting genre",max_length=30)
    description = models.TextField(default="awaiting description")
    picture = models.ImageField(upload_to='pictures/%d/%m/%Y/', blank=True)
    imdb_score = models.FloatField(default=0.0)
    price = models.FloatField(default=3.90)
    quantity_stock = models.IntegerField(default=10)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
