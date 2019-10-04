from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import PedidoForm, ClienteForm
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import get_object_or_404


# Create your views here.
def inicio(request):
    return render(request, 'wans/index.html', {})


def trabajos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'wans/lista.html', {'pedidos': pedidos})


def new_pedido(request):
    #user = get_object_or_404(User, pk=user_id)
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
        cliente = cliente_form.save(commit=False)
        dni_repetido = Cliente.objects.filter(dni=cliente.dni).exists()
        if user_form.is_valid() and cliente_form.is_valid() and not dni_repetido:
            user = user_form.save()
            cliente.usuario = user
            clientes = Group.objects.get(name='Clientes')
            clientes.user_set.add(cliente.usuario)
            cliente.save()
            return redirect('login')
        elif dni_repetido:
            cliente_form.dni_error = 'Error: DNI ya registrado'
    else:
        user_form = UserCreationForm()
        cliente_form = ClienteForm()
    return render(request, 'registration/singup.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })

