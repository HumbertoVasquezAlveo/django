""" Modelo de categorias"""

from django.db import models

#importando el modelo Product
from products.models import Product

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    # Product es el modelo con el cual se quiere realizar la relacion
    Products = models.ManyToManyField(Product, blank=True) 
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
