from django.urls import path
from . import views


urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('signup/', views.signup, name='signup'),
	path('trabajos/', views.trabajos, name='trabajos'),
	path('nuevopedido/', views.new_pedido, name='new_pedido'),
	path('perfil/', views.perfil, name='perfil')
]