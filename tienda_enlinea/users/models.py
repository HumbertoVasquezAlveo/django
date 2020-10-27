""" Modelo proxy de Usuarios"""

from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstracUser
#Modelo User creado por nosotros (sin usar el default por Django)
class User(AbstractUser):
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    
class Customer(User):
    class Meta:
        
        # no permite que se cree una nueva tabla
        proxy = True 
        
    def get_products(self):
        return []

class Profile(models.Model):
    """ Relacion Uno a Uno con el usuario"""
    
    #indica a django que cuando se elimine el usuario tambien se elimine el registro profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio  = models.TextField()