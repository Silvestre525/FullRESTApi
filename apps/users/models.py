from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


    