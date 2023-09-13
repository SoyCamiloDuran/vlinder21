from django.shortcuts import render,redirect

from .carro import Carro
from menu.models import Producto
from .forms import InfoPedidoForm


# Create your views here.
def carrito(request):
    if request.method == 'GET':
        contacto_form = InfoPedidoForm()
        return render(request, 'carro/carro.html', {'contacto_form' : contacto_form})
    
    if request.method == 'POST':
        contacto_form = InfoPedidoForm(request.POST)
        if contacto_form.is_valid():
            # Aqui iran todas las acciones a realizar cuando los datos son correctos
            pass
        else:
            # Aqui comunicamos al usuairo que los datos no son validos
            return render(request, 'carro/carro.html', {'contacto_form' : contacto_form})

    return render(request, 'carro/carro.html', {})

def agregar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    
    return redirect("carro:carro")



def eliminar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.eliminar_carrito(producto=producto)
    
    return redirect("carro:carro")





def restar_producto(request,producto_id):
    carro= Carro(request)
    producto= Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)
    
    return redirect("carro:carro")


def limpiar_carroproducto(request):
    carro= Carro(request)
    carro.limpiar_carrito()
    
    return redirect("carro:carro")


    




