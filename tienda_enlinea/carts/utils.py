from .models import Cart 

""" Funcion de creacion del carrito de compras"""
def get_or_create_cart(request):
    #Crear una sesion / la sesion se crea en el objeto request, se envia al cliente y se obtiene en cada peticion
    #la petecion esta en constante interaccion entre cliente y servidor
    
    # si el usuario esta autenticado entinces se obtendra el usuario actual, de lo contrario NONE, puede o no pertenecer
    # a un usuario. Todo depende si esta autentocado o no.
    #request.session['cart_id'] = None
    
    # Creando el carrito de compras apartir de la sesion
    user = request.user if request.user.is_authenticated else None # si el usuario esta autenticado entonces obtenemos el usuario actual, en caso contrario None
    cart_id = request.session.get('cart_id') # diccionario session retorna None en caso la llave no exista.
    #obtencion del carrito
    cart = Cart.objects.filter(cart_id=cart_id).first()
    
    # Si no existe el carrtito
    if cart is None:
        
    # se crea uno nuevo
        cart = Cart.objects.create(user=user)
        
    #Asignar un usuario al carrito de compras despues de la autenticacion
    # Si el usuario existe y el carrito no posee un usuario, entonces se crea la relacion, se asigna y se guarda.
    if user and cart.user is None:
        cart.user = user
        cart.save()
         
    #Actulisacion de la sesion    
    request.session['cart_id'] = cart.cart_id
    
    return cart
    
    # Mencion:
    # Si la peticion se encuentra en la sesion, entonces obtendremos el carrito de compras de la Base de Datos
    # de lo contrario, creamos un nuevo carrito.