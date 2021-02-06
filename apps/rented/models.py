from django.db import models
from apps.clients.models import Client
from django.contrib.auth.models import User
import datetime


class Rent (models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    movie_name = models.CharField(default='', max_length=80)
    cpf = models.CharField(default='', max_length=14)
    date_start = models.DateField(datetime.datetime.now())
    date_end = models.DateField(datetime.datetime.now())
    def __str__(self):
        return self.user.username

