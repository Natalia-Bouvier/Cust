from django.db import models
from empresa.models import Empresa

#class Empresa (models.Model):
    #logo= models.ImageField(name=logo)
    #rut = models.CharField(max_length=25, default='rut de la empresa')
    #razon_social = models.CharField(max_length=50, default='razón social de la empresa')
    #direccion = models.CharField(max_length=200, default='Dirección de la empresa')
    #telefono = models.CharField(max_length=9, default='Teléfono de la empresa')

class Cliente (models.Model):
    Nombre = models.CharField(max_length=35, default="")
    fecha_nacimiento = models.DateField(auto_now=True)
    direccion = models.CharField(max_length=200,default='Dirección del cliente')
    sexo = models.IntegerField(choices=((1, ("Femenino")),
                                        (2, ("Masculino"))),
                                        default=1)
    telefono = models.CharField(max_length=9,default='Teléfono del cliente')
    correo = models.EmailField(max_length=255,default='example@email.com')
    cedula = models.CharField(max_length=15,default='1.111.111-1')
    Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, null=True)
    observaciones= models.CharField(max_length=1000, default="")
   

    def __str__(self):
       return self.Nombre

