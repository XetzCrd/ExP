from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'tiendas'

urlpatterns = [
    path('', lambda request: redirect('/gestionTienda', permanent=False)),
    path('gestionTienda', views.gestionTienda, name='gestionTienda'), #ver las tiendas por defecto
    #path('verTienda/<str:idTienda>', views.verTienda, name='verTienda'),
    path('eliminarTienda/<str:idTienda>', views.eliminarTienda, name='eliminarTienda'),
    path('asignarTienda', views.asignarTienda, name='asignarTienda'),
    
    path('Productos', views.productos, name='productos'),
    path('eliminarProducto/<str:idProducto>', views.eliminarProducto, name='eliminarProducto'),
    path('asignarProducto', views.asignarProducto, name='asignarProducto'),

    path('verTienda/<str:idTienda>/', views.verTienda, name='verTienda'),
    path('eliminarProductoTienda/<str:idProducto>', views.eliminarProductoTienda, name='eliminarProductoTienda'),   
]