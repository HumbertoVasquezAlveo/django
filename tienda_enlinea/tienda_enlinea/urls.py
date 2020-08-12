from django.contrib import admin
from django.urls import path

#Views
from . import views


urlpatterns = [
    #vacio por que es la url de inicio
    path('',views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.login_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
]
