from django.contrib import admin

# Register your models here.
from .models import Animal,Colaborador, Protectora

admin.site.register(Animal)
admin.site.register(Colaborador)
admin.site.register(Protectora)