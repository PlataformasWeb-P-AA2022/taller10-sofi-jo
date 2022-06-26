from django.db import models

# Create your models here.

class Parroquia(models.Model):
    opciones_parroquia =(
        ('urbano','Urbano'),
        ('rural','Rural')
    )
    nombre = models.CharField(max_length=30)
    
    tipo = models.CharField(max_length=30, choices=opciones_parroquia)

    def __str__(self):
        return "%s %s" % (self.nombre, 
                          self.tipo)


class  Barrio(models.Model):
    numero_par =((1,'1'),(2,'2'),(3,'3'),(4,'4'),
    (5,'5'),(6,'6'))

    nombre = models.CharField(max_length=30)
    numero_vivien = models.IntegerField('numero de viviendas')
    numero_par = models.IntegerField(
    choices = numero_par)
    numero_edif = models.IntegerField('numero de edificios')

    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,
    related_name= "barrios")
    
    def __str__(self):
        return "%s %d %d %d" % (self.nombre, 
                self.numero_vivien,
                self.numero_par,
                self.numero_edif)