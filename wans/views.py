from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import PedidoForm, ClienteForm, CV
from django.contrib.auth.models import User, Group
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import get_object_or_404


# Create your views here.
def inicio(request):
    usuario = request.user
    grupos = usuario.groups.all
    return render(request, 'wans/index.html', {'grupos': grupos})


def trabajos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'wans/lista.html', {'pedidos': pedidos})


def pedido_enviado(request, pk):
    pedido = Pedido.objects.get(pk=pk)
    return render(request, 'wans/pedido_enviado.html', {'cliente': pedido.usuario})


def new_pedido(request):
    cliente = Cliente.objects.get(usuario=request.user)
    cliente = cliente.nombre
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            return redirect('pedido_enviado', pk=pedido.id)
    else:
        form = PedidoForm()
    return render(request, 'wans/pedido.html', {'form': form, 'cliente': cliente})


def new_tecnico(request):
    cliente = get_object_or_404(Cliente, usuario=request.user)
    if request.method == 'POST':
        form = CV(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user
            grupo = Group.objects.get(name='A revisar')
            grupo.user_set.add(cliente.usuario)
            cliente.save()
            return redirect('inicio')
    else:
        form = CV()
    return render(request, 'wans/new_tecnico.html', {'form': form})


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


def agregar_a_grupo(request, user_id):
    usuario = User.objects.filter(id=user_id)
    tecnicos = Group.objects.get(name='Tecnicos')
    revision = Group.objects.get(name='A revisar')
    tecnicos.user_set.add(usuario[0])
    revision.user_set.remove(usuario[0])
    return redirect('inicio')


def sacar_de_grupo(request, user_id):
    usuario = User.objects.filter(id=user_id)
    grupo = Group.objects.get(name='A revisar')
    grupo.user_set.remove(usuario[0])
    return redirect('inicio')


def revisar(request):
    clientes = Cliente.objects.filter(usuario__groups__name='A revisar')
    return render(request, 'wans/revisar.html', {'clientes': clientes})


def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.delete()
    return redirect('trabajos')


def pedido_detalle(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'wans/pedido_detalle.html', {'pedido':pedido})