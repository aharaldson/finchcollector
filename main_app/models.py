from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    kind = models.CharField(max_length=100)

def __str__(self):
    return self.name