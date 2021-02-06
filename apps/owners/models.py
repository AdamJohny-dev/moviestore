from django.db import models
from django.contrib.auth.models import User

class Owner (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    type_user = models.CharField(default="owner", max_length=10)
    def __str__(self):
        return self.name
    