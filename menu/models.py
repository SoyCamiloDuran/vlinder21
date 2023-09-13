from django.db import models

class Tipo(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    descripcion = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    descripcion = models.TextField(max_length=1000, null=True, blank=True)
    precio = models.IntegerField(null=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='get_posts')
    img = models.ImageField(default='../../static/img/logovlinder.jpg', upload_to="img-producto")
    
    def __str__(self):
        return self.nombre



