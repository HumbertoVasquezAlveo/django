""" View Products."""

#Django
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#Models
from .models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    
    
    
    # se encarga de pasar el contexto de la clase al template(index)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #--> pasando el contexto de la clase Padre
        context['message'] = 'Listado de productos'  #--> 
        
        print(context)
        
        return context
    
    
    
class ProductDetailView(DetailView): #--> Obtenda datos de la DB por id -> LLave primaria
    model = Product
    template_name = 'products/product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #--> pasando el contexto de la clase Padre
        
        
        print(context)
        
        return context

# todas las clases que hereden de ListView deben de tener template_name y queryset
# dependemos del atributo "q" del formulario nos envie

class ProductSearchListView(ListView):
    template_name = 'products/search.html'
    
    # consulta de busqueda por titulo y compara con valor de "q" que esta en el queryset
    # comparacion con la busqueda, busqueda por titulo
    #1
                 #CONSULTA DE BUSQUEDA
    def get_queryset(self):
        
        #query SQL = SELECT * FROM products WHERE title like %valor%
        #i = indica que NO es sensible para M o m
        return Product.objects.filter(title__icontains=self.query())
    
    #2
    def query(self):
        return self.request.GET.get('q')
    
    # para acceder al valor de la busqueda escrita en la barra de busqueda.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['query'] = self.query()
        
        #traer la cantidad de elementos, traemos la cantidad de elementos y luego lo contamos
        context['count'] = context['product_list'].count() #--> 
        
        return context
        
        print(context)
    
    
    
    
        
        
    
    
