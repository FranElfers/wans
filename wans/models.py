from django.db import models


# Create your models here.
class Cliente(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    presentacion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=6)

    def __str__(self):
        return self.cliente
