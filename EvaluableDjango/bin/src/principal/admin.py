'''
Created on 11/05/2015

@author: luis
'''
from principal.models import Actor,Director,Pelicula
from django.contrib import admin


admin.site.register(Pelicula) #dar de alta la tabla en el administrador para que nos salga para rellenar las tablas
admin.site.register(Actor)
admin.site.register(Director)