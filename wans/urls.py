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
    path('revisar/', views.revisar, name='revisar'),
    path('pedido/<int:pk>', views.pedido_detalle, name='pedido_detalle'),
    #path('finalizar/<int:pk>/', views.finalizar_pedido, name='finalizar_pedido'),
    path('enviado/<int:pk>/', views.pedido_enviado, name='pedido_enviado'),
    path('historial/', views.historial, name='historial')
]
