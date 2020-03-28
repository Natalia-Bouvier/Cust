from django.db import models

# Create your models here.
class Empresa (models.Model):
    #logo= models.ImageField(name=logo)
    #Nombre = models.CharField(max_length=35, default="")
    rut = models.CharField(max_length=25, null=True)
    razon_social = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=9, null=True)
    def __str__(self):
       return self.razon_social

class Colaborador (models.Model):
    Nombre = models.CharField(max_length=35, default="")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200,null=True)
    #sexo = models.IntegerField(choices=((1, ("Femenino")),
    #                                    (2, ("Masculino"))),
    #                                    default=1)
    #sexo = (('F','Femenino'),('M','Masculino'),)
    sexo = (('Femenino','Femenino'),('Masculino','Masculino'),)
    sexo = models.CharField(max_length = 10, choices = sexo)

    telefono = models.CharField(max_length=9,null=True)
    correo = models.EmailField(max_length=255,null=True)
    cedula = models.CharField(max_length=15,null=True)
    Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, null=True)
    Observaciones = models.CharField(max_length=1000, default="")

    def __str__(self):
       return self.Nombre
