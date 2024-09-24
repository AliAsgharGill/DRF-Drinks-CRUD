from django.db import models
from django.db.models.manager import Manager
from django.contrib.auth.models import User
class Drink(models.Model):
    objects: Manager = models.Manager() # write this line to solve the no member 'objects' error
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name+ ", " +self.description
    

class UserLogin(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username