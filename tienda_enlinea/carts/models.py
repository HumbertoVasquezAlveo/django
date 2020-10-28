""" Modelo del carrito de compras """

#Django
from django.db import models

#Modelos
from users.models import User
from products.models import Product

# El carrito de compras tendra una relacion con el modelo User, de Uno a muchos
# No estara restringido que solo los usuarios autenticados puedan hacer su carrito de compras

class Cart(models.Model):
    #ForeignKey = establece una relacion, uno a muchos.
    #CASCADE =  indica que cuando se borre un usuario, tambien se eliminen sus relaciones.
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return ''
    
