from django.urls import path
from . import views

urlpatterns = [
    path('contanto/', views.contacto, name="contacto")
]
