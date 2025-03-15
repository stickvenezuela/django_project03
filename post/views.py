from django.shortcuts import render
from django.views.generic import ListView #este comando es para importar la clase ListView
from post.models import Post 


# Create your views here.
class PostListView(ListView): #ListView es una clase que permite listar objetos de un modelo en una vista
    model=Post #modelo que se va a listar en una vista
    template_name='post.html' #nombre del template que se va a renderizar en la vista 

# Buscar diferencia entre clase y función de python porque se pueden hacer de las dos maneras. 
# En este caso estamos trabajando con una clase. 