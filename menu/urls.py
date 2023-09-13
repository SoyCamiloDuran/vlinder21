from django.urls import path
from . import views


urlpatterns = [
    path('productos/', views.productos, name="productos"),
    path('productos/<int:id>', views.productos, name="productos"),
]
