from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    if request.method == 'GET':
        contacto_form = ContactoForm()
        return render(request, 'forms/contacto.html', {'contacto_form' : contacto_form})
    
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            # Aqui iran todas las acciones a realizar cuando los datos son correctos
            pass
        else:
            # Aqui comunicamos al usuairo que los datos no son validos
            return render(request, 'forms/contacto.html', {'contacto_form' : contacto_form})

 
