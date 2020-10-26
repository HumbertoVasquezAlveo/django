""" URL's correspondientes a la Aplicacion Products. """

#Django
from django.urls import path

#Views 
from . import views


urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name="search"),
    
    # Vista que permite buscar desde el valor (q) en el queryset
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
    
]