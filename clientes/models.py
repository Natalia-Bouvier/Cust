from django.db import models
from empresa.models import Empresa


class Cliente (models.Model):
    Nombre = models.CharField(max_length=35, default="")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200,null=True)
    # sexo = models.IntegerField(choices=((1, ("Femenino")),
    #                                     (2, ("Masculino"))),
    #                                     default=1)
    sexo = (('Femenino','Femenino'),('Masculino','Masculino'),)
    sexo = models.CharField(max_length = 10, choices = sexo)
    telefono = models.CharField(max_length=9,null=True)
    correo = models.EmailField(max_length=255,null=True)
    cedula = models.CharField(max_length=15,null=True)
    Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, null=True)
    observaciones= models.CharField(max_length=1000, default="")

    def __str__(self):
       return self.Nombre
