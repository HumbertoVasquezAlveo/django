"""Views inicial."""

#Django
from django.http import HttpResponse
from django.shortcuts import render

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
def login(request):
    return render(request, 'users/login.html',{
        #context
    })