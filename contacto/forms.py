from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, widget=forms.TextInput(attrs={'class' : 'campo w-100 campo-nombre'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class' : 'campo  w-100 campo-email'}))
    comentario = forms.CharField(label='Comentario', widget=forms.Textarea(attrs={'class' : 'campo  w-100 campo-comentario'}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre != "Open":
            raise forms.ValidationError("Malo")
        else:
            return nombre