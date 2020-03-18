from django.db import models
from  empresa.models import Empresa
from  empresa.models import Colaborador
from  clientes.models import Cliente

class CategoriaServicio (models.Model):
    tipo_de_servicio = models.CharField(max_length=20,default="servicio")
    Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
       return self.tipo_de_servicio
       
class Servicio (models.Model):
    fecha_hora = models.DateField(auto_now=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True)
    tipo_de_servicio = models.ForeignKey(CategoriaServicio, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
       return self.tipo_de_servicio