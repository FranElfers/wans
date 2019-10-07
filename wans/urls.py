from django.urls import path
from . import views


urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('signup/', views.signup, name='signup'),
	path('trabajos/', views.trabajos, name='trabajos'),
	path('nuevopedido/', views.new_pedido, name='new_pedido'),
	path('perfil/', views.perfil, name='perfil'),
	path('nuevotecnico/', views.new_tecnico, name='new_tecnico'),
	path('add/<int:user_id>/', views.agregar_a_grupo, name='agregar_a_grupo'),
	path('remove/<int:user_id>/', views.sacar_de_grupo, name='sacar_de_grupo'),
	path('mandarcv/', views.mandar_cv, name='mandar_cv'),
	path('revisar/', views.revisar, name='revisar'),
	path('eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido')
]