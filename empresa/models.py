from django.db import models

# Create your models here.
class Empresa (models.Model):
    #logo= models.ImageField(name='logo')
    Nombre = models.CharField(max_length=35, default="")
    rut = models.CharField(max_length=25, null=True)
    razon_social = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=9, null=True)
    correo = models.EmailField(max_length=255, null=True)

    def __str__(self):
       return self.Nombre