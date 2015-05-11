#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    fecha_de_nacimiento= models.DateField()
    categorias_preferidas= models.TextField()

class Actor(models.Model):
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    biografia= models.TextField()
    peliculas= models.TextField(help_text='Peliculas en las que actua')
    
    
    def __unicode__(self):
        return self.nombre+" "+self.apellidos
    
class Director(models.Model):
    nombre= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=100)
    biografia= models.TextField()
    peliculas= models.TextField(help_text='Peliculas dirigidas')
   # pelicula= models.ManyToManyField(Pelicula)
   
    def __unicode__(self):
        return self.nombre+" "+self.apellidos


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    #anio = models.CharField(max_length=4)
    anio = models.DecimalField(max_digits=4,decimal_places=0,help_text="Maximo 4 digitos")
    actores_principales = models.ManyToManyField(Actor,related_name='actores_peliculas')
    directores= models.ManyToManyField(Director,related_name='directores_peliculas')
    resumen= models.TextField(help_text="Sipnosis")
    categorias= models.TextField()
    #puntuacion= models.ManyToManyField(Usuario,through='Puntuacion')
    UNO = 'UN'
    DOS = 'DO'
    TRES = 'TR'
    CUATRO = 'CU'
    CINCO= "CI"
    PUNTUACIONES = (
        (UNO, '1'),
        (DOS, '2'),
        (TRES, '3'),
        (CUATRO, '4'),
        (CINCO, '5')
    )
    puntuacion = models.CharField(max_length=2,
                                      choices=PUNTUACIONES,
                                      default=UNO)
 

    def __unicode__(self):
        return self.titulo

'''class Puntuacion(models.Model):
    usuario= models.ForeignKey(Usuario)
    pelicula=models.ForeignKey(Pelicula)
    
    UNO = 'UN'
    DOS = 'DO'
    TRES = 'TR'
    CUATRO = 'CU'
    CINCO= "CI"
    PUNTUACIONES = (
        (UNO, '1'),
        (DOS, '2'),
        (TRES, '3'),
        (CUATRO, '4'),
        (CINCO, '5')
    )
    puntuacion = models.CharField(max_length=2,
                                      choices=PUNTUACIONES,
                                      default=UNO)'''




    

    
    

    

