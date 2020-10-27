""" Administrador de la App Category """

from django.contrib import admin
from.models import Category


# Registrando el modelo Category en el Sitio Administrador.
admin.site.register(Category)