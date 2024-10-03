from django.shortcuts import render
from .models import Animal, Colaborador, Protectora

# Create your views here.
def animal_list(request):
    posts = Animal.objects.all()
    return render(request, 'Animales/animal_list.html',{"animal_mostrar":posts})

def colaborador_list(request):
    posts = Colaborador.objects.all()
    return render(request, 'Colaborador/colaborador_list.html',{"colaborador_mostrar":posts})

def protectora_list(request):
    posts = Protectora.objects.all()
    return render(request, 'Protectora/protectora_list.html',{"protectora_mostrar":posts})