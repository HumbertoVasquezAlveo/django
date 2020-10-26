"""Views inicial."""

#Django
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User 

from .forms import RegisterForm
from products.models import Product

#request parametro
def index(request):
    
    # Muestra los productos y como se muestra
    products = Product.objects.all().order_by('-id')
    
    #tres argumentos, = la peticion, el template y el template
    return render(request,'index.html',{
        
        #context
        #puedo usar la variable message desde el template
        'message':'Lista de productos',
        'title' : 'Productos',    
        'products': products,
    })
 
#request es la peticion   
def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    #print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # la funcion authenticate buscara en BD un usuario y contraseña existente, luego se preguntara
        # si user usando login pasandole los argumentos request, user. si esto es cierto sera cierto si no sera falso
        user = authenticate(username=username, password=password)
        if user:
            login(request, user) # --> creando la sesion
            #enviando del server al cliente y message para enviar mensj usddo en el index
            messages.success(request, 'Bienvendo {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no valida')
            
    return render(request, 'users/login.html',{
        #context
    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')


def register(request):
    
    # validacion para bloquear
    if request.user.is_authenticated:
        return redirect('index')
    
    # por defecto este dato (clase RegisterForm) viene vacio, lo podemos forzar creando un diccionario con datos
    #instancia del formulario
    
    # si por metodo post envia los datos si no, No envies nada (vacio).
    form = RegisterForm(request.POST or None) 
    
    # permite conocer si la informacion es valida (si es por metodo POST y es valiudo toma los atributos de nuestro formulario)
    if request.method == 'POST' and form.is_valid():
        
        #usando el modelo de usuario User de django
        #llamando al metodo save
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        
    #condicionar
    
    return render(request, 'users/register.html', {
        #context
        'form':form
    })
