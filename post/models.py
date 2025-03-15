from django.db import models

# Create your models here.
# Paso 1: Crear el modelo Post


# Estructura de modelo 
class Post(models.Model):
    # campos del modelo (atributos del modelo)
    title= models.CharField(max_length=100) 
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images/', blank=True) #blank=true significa que el campo no es obligatorio
    def __str__(self): 
        return self.title 