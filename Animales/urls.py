from django.urls import path
from . import views

urlpatterns = [
    path('Animales/', views.animal_list, name="animal_list"),
    path('Colaborador/', views.colaborador_list, name="colaborador_list"),
    path('Protectora/', views.protectora_list, name="protectora_list")
]