""" General URL's."""

#Django
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings


#Views
from . import views

#Models
from products.views import ProductListView

urlpatterns = [
    #vacio por que es la url de inicio
    path('',ProductListView.as_view(), name='index'), # udsando la clase ProductListView como una vista
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    
    # Declarando las URL's de la Aplicacion Productos
    path('productos/', include('products.urls')),
    
    # Declarando las URL's de la Aplicacion Carrito de compras
    path('carrito/', include('carts.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
