""" Vista del carrito de compras """

#Django
from django.shortcuts import render
from django.shortcuts import redirect

#Modelos
from .models import Cart
from products.models import Product

#Utilidades
from .utils import get_or_create_cart


#funcion del carrito de compras
def cart(request):
    cart = get_or_create_cart(request)
    
    return render(request, 'carts/cart.html', {
        # Enviar el objeto cart al template, para visualizar los productos en el carrito 
        'cart':cart
    })

#funcion para agregar productos al carrito de compras    
def add(request):
    #obteniendo el carrito de compras
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id')) # product_id = llave
    
    #Agregar productos al carrito de compras(modelo cart posee una relacion a productos ManyToMany)
    cart.products.add(product)
    
    return render(request, 'carts/add.html', {
        #contexto
        'product':product
    })

# Funcion para eliminar productos del carrito de compras    
def remove(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    
    # Seleccionamos el objeto a eliminar --> product
    cart.products.remove(product)
    
    return redirect('carts:cart')