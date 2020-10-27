"""Administrador de Usuarios"""

from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Registrando el Modelo Abstracto del Usuario

admin.site.register(User, UserAdmin)
