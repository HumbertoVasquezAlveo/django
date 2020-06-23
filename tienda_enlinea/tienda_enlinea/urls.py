from django.contrib import admin
from django.urls import path

#Views
from . import views



urlpatterns = [
    #vacio por que es la url de inicio
    path('',views.index, name='index'),
    path('usuarios/login', views.login, name='login'),
    path('admin/', admin.site.urls),
]
