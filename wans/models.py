from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField(null=True)
    curriculum = models.TextField(max_length=3000, null=True)

    def __str__(self):
        return self.usuario.username


class Pedido(models.Model):
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    presentacion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    latitud = models.FloatField(default=0.0)
    longitud = models.FloatField(default=0.0)
    dificultad = models.CharField(max_length=6)

    def __str__(self):
        return self.ubicacion
