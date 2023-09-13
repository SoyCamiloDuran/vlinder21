from django.shortcuts import render, get_object_or_404
from .models import Tipo, Producto

def productos(request, id = 1):
    filtros = Tipo.objects.all()
    if id != 1:
        todos = Producto.objects.filter(tipo_id = id)
    else:
        todos = Producto.objects.all().order_by('id')

    return render(request, 'menu/productos.html', {'filtros' : filtros, 'todos' : todos})


    


