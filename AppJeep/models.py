from django.db import models

# Create your models here.
class Jeeps(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    motor = models.CharField(max_length=15)
    cilindrada = models.CharField(max_length=30)
    patente = models.CharField(max_length=30)
    año = models.CharField(max_length=30)