from django.db import models

# Create your models here.
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    anio_publicacion = models.PositiveIntegerField()
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def __str__(self):
        return self.titulo
