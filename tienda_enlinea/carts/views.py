""" Vista del carrito de compras """

#Django
from django.shortcuts import render

#Modelos
from .models import Cart

#funcion del carrito de compras
def cart(request):
    
    #Crear una sesion / la sesion se crea en el objeto request, se envia al cliente y se obtiene en cada peticion
    #la petecion esta en constante interaccion entre cliente y servidor
    
    # si el usuario esta autenticado entinces se obtendra el usuario actual, de lo contrario NONE, puede o no pertenecer
    # a un usuario. Todo depende si esta autentocado o no.
    
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        # Obtendremos el carrito de la base de datos, filtrando por primary key
        cart = Cart.objects.get(pk=request.session.get('cart_id'))
    else:
        cart = Cart.objects.create(user=user)
       
    # la session esta almacenando el id del carrito    
    request.session['cart_id'] = cart.id
    
    return render(request, 'carts/cart.html', {
        
    })
    
    # Mencion:
    # Si la peticion se encuentra en la sesion, entonces obtendremos el carrito de compras de la Base de Datos
    # de lo contrario, creamos un nuevo carrito.