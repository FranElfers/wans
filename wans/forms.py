from django import forms
from .models import Pedido, Cliente


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('usuario', 'dificultad', 'presentacion', 'ubicacion')


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'dni')
