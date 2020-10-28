""" Administrador del Carrito de compras"""

#Django
from django.contrib import admin

# Modelos 
from .models import Cart

#Sitios a registrar

admin.site.register(Cart)
