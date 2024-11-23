from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'crud/index.html', {'libros': libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, 'crud/detail.html', {'libro': libro})
