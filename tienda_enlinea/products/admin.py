from django.contrib import admin


# --> registrando el modelo en el Admin
from .models import Product


# Configurar que queremos que se muestre en el Administrador (Productos)

class ProductAdmin(admin.ModelAdmin):
    
    # Campos que queremos que se muestren en el Administrador
    fields = ('title','description','price','image')
    list_display = ('__str__', 'slug', 'created_at')
    

admin.site.register(Product, ProductAdmin)