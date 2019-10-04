from django import forms
from .models import Pedido, Cliente


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('presentacion', 'ubicacion')


class ClienteForm(forms.ModelForm):

    dni_error = ''

    class Meta:
        model = Cliente
        fields = ('nombre', 'dni')
