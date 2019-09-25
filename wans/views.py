from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import PedidoForm


# Create your views here.
def inicio(request):
    return render(request, 'wans/index.html', {})


def trabajos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'wans/lista.html', {'pedidos': pedidos})


def new_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user
            pedido.dificultad = '***'
            pedido.save()
            return redirect('inicio')
    else:
        form = PedidoForm()
    return render(request, 'wans/pedido.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registration/singup.html', {'form': form})
