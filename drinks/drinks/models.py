from django.db import models
from django.db.models.manager import Manager
class Drink(models.Model):
    objects: Manager = models.Manager() # write this line to solve the no member 'objects' error
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name+ ", " +self.description