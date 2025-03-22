from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Género")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"


class Director(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del director")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True)
    biografia = models.TextField(verbose_name="Biografía", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"


class Actor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del actor")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True)
    biografia = models.TextField(verbose_name="Biografía", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actores"


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    sinopsis = models.TextField(verbose_name="Sinopsis")
    fecha_estreno = models.DateField(verbose_name="Fecha de estreno")
    duracion = models.PositiveIntegerField(verbose_name="Duración (minutos)")
    generos = models.ManyToManyField(Genero, related_name="peliculas", verbose_name="Géneros")
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Director")
    actores = models.ManyToManyField(Actor, related_name="peliculas", verbose_name="Actores")
    imagen = models.ImageField(upload_to="peliculas/", null=True, blank=True, verbose_name="Imagen de portada")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"