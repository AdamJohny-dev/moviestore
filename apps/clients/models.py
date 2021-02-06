from django.db import models
from django.contrib.auth.models import User


class Client (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=14)
    type_user = models.CharField(default="client", max_length=10)
    def __str__(self):
        return self.name

   
    
  
    
