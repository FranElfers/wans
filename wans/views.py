from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import PedidoForm, ClienteForm
from django.shortcuts import get_object_or_404


# Create your views here.
def inicio(request):
    return render(request, 'wans/index.html', {})


def trabajos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'wans/lista.html', {'pedidos': pedidos})


def new_pedido(request):
    # user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.dificultad = '***'
            pedido.usuario = request.user
            pedido.save()
            return redirect('inicio')
    else:
        form = PedidoForm()
    return render(request, 'wans/pedido.html', {'form': form})


def perfil(request):
    return render(request, 'wans/perfil.html', {})


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.usuario = user
            cliente.save()
            return redirect('inicio')
    else:
        user_form = UserCreationForm()
        cliente_form = ClienteForm()
    return render(request, 'registration/singup.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })
