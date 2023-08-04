from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tiendaInfo, productoInfo

# TIENDAS

def gestionTienda(request):

    if request.method == 'POST':
        direccion = request.POST.get('direccionTienda')
        provincia = request.POST.get('provinciaTienda')
        region = request.POST.get('regionTienda')
        telefonoContacto = request.POST.get('telefonoTienda')
        tiendaInfo.objects.create(
            direccion=direccion,
            provincia=provincia,
            region=region,
            telefonoContacto=telefonoContacto
        )
        return HttpResponseRedirect(reverse('tiendas:gestionTienda'))

    return render(request, 'gestionTienda.html', {
        'tiendasTot': tiendaInfo.objects.all().order_by('id'),
        'productosTot': productoInfo.objects.all().order_by('id'),
    })

def eliminarTienda(request, idTienda):
    tiendaEliminar = tiendaInfo.objects.get(id=idTienda)
    tiendaEliminar.delete()
    return HttpResponseRedirect(reverse('tiendas:gestionTienda'))

def asignarTienda(request):
    if request.method == 'POST':
        idProducto = request.POST.get('productoSeleccionado')
        idTienda = request.POST.get('tiendaSeleccionada')

        objProducto = productoInfo.objects.get(id=idProducto)
        objTienda = tiendaInfo.objects.get(id=idTienda)     
        
        objTienda.productoinfo_set.add(objProducto)
        
    return HttpResponseRedirect(reverse('tiendas:gestionTienda'))


### PRODUCTOS

def productos(request):

    if request.method == 'POST':
        descripcion = request.POST.get('descripcionProducto')
        codigo = request.POST.get('codigoProducto')
        precioVenta = request.POST.get('precioProducto')
        cantidad = request.POST.get('cantidadProducto')
        productoInfo.objects.create(
            descripcion=descripcion,
            codigo=codigo,
            precioVenta=precioVenta,
            cantidad=cantidad
        )
        return HttpResponseRedirect(reverse('tiendas:productos'))

    return render(request, 'Productos.html', {
        'tiendasTot': tiendaInfo.objects.all().order_by('id'),
        'productosTot': productoInfo.objects.all().order_by('id'),
    })

def eliminarProducto(request, idProducto):
    productoEliminar = productoInfo.objects.get(id=idProducto)
    productoEliminar.delete()
    return HttpResponseRedirect(reverse('tiendas:productos'))

def asignarProducto(request):
    if request.method == 'POST':
        idProducto = request.POST.get('productoSeleccionado')
        idTienda = request.POST.get('tiendaSeleccionada')

        objProducto = productoInfo.objects.get(id=idProducto)
        objTienda = tiendaInfo.objects.get(id=idTienda)

        objProducto.tiendaRelacionada = objTienda
        objProducto.save()

    return HttpResponseRedirect(reverse('tiendas:productos'))



### VER TIENDA
def verTienda(request, idTienda):
    cache.set('idTienda',idTienda)
    
    tiendaSeleccionada = tiendaInfo.objects.get(id=idTienda)
    productosTienda = tiendaSeleccionada.productoinfo_set.all().order_by('id')

    context = {
        'tiendaSeleccionada': tiendaSeleccionada,
        'productosTot': productosTienda
    }
    return render(request, 'verTienda.html', context)

def eliminarProductoTienda(request, idProducto):
    
    idTienda = cache.get('idTienda')
    productoSeleccionado = productoInfo.objects.get(id=idProducto)
    tiendaSeleccionada = tiendaInfo.objects.get(id=idTienda)
    
    tiendaSeleccionada.productoinfo_set.remove(productoSeleccionado)
    

    return verTienda(request, idTienda)
 