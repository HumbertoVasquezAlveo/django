""" Modelo del carrito de compras """
import uuid
#Django
from django.db import models
from django.db.models.signals import pre_save

#Modelos
from users.models import User
from products.models import Product

# El carrito de compras tendra una relacion con el modelo User, de Uno a muchos
# No estara restringido que solo los usuarios autenticados puedan hacer su carrito de compras

class Cart(models.Model):
    #ForeignKey = establece una relacion, uno a muchos.
    #CASCADE =  indica que cuando se borre un usuario, tambien se eliminen sus relaciones.
     #cart_id = crea un identificador unico para cada sesion, string alfanumerico
     
    cart_id = models.CharField(max_length=100, null=False, blank=True, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # Identificador unico
        return self.cart_id
 
# Creando un indentificador unico para nuestro carrito de compras
# Esta funcion es un callback   
def set_cart_id(sender, instance, *args, **kwargs):
    #crear un carrito si y solo si no existe uno
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())
        
pre_save.connect(set_cart_id, sender=Cart)