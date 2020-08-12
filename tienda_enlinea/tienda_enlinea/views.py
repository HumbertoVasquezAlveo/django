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

#request parametro
def index(request):
    #tres argumentos, = la peticion, el template y el template
    return render(request,'index.html',{
        
        #context
        #puedo usar la variable message desde el template
        'message':'Lista de productos',
        'title' : 'Productos',    
        'products': [
            {'title':'Playera','price':5, 'stock': True},
            {'title':'Camisa','price':10, 'stock': True},
            {'title':'Mochila','price':20, 'stock': False},
        ]
    })
 
#request es la peticion   
def login_view(request):
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
    # por defecto este dato (clase RegisterForm) viene vacio, lo podemos forzar creando un diccionario con datos
    #instancia del formulario
    
    # si por metodo post envia los datos si no, No envies nada (vacio).
    form = RegisterForm(request.POST or None) 
    
    # permite conocer si la informacion es valida (si es por metodo POST y es valiudo toma los atributos de nuestro formulario)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        #usando el modelo de usuario User de django
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
                
        print(username)
        print(email)
        print(password)    
    #condicionar
    
    return render(request, 'users/register.html', {
        #context
        'form':form
    })
