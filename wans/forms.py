from django import forms
from .models import Pedido, Cliente


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('presentacion', 'ubicacion', 'latitud', 'longitud', 'dificultad')


class CV(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('curriculum',)


class ClienteForm(forms.ModelForm):
    dni_error = ''

    class Meta:
        model = Cliente
        fields = ('nombre', 'dni')


class FinalizarForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('finalizado',)
