from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    presentacion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=6)

    def __str__(self):
        return self.cliente
