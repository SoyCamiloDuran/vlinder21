from django import forms

class InfoPedidoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, widget=forms.TextInput(attrs={'class' : 'campo w-100 campo-nombre'}))
    direccion = forms.CharField(label='Direccion', max_length=100, widget=forms.TextInput(attrs={'class' : 'campo  w-100 campo-direccion'}))
    numero_contacto = forms.CharField(label='Numero de contacto', max_length=12 , widget=forms.TextInput(attrs={'class' : 'campo  w-100 campo-contacto'}))
    CHOICES = (
        ('1' , 'Efectivo'),
        ('2' , 'Transferencia')
    )
    metodo_pago = forms.CharField(label='Metodo de pago', widget=forms.Select(attrs={'class' : 'campo  w-100 campo-pago'}, choices=CHOICES))

   