from django.contrib import admin
from .models import Pelicula, Genero, Director, Actor
# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Actor)