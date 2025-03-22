from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Pelicula

# Create your views here.
class MoviesView(ListView):
    template_name = 'movies.html'
    model = Pelicula