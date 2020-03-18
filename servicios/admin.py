from django.contrib import admin

# Register your models here.
from .models import Servicio
admin.site.register(Servicio)

from .models import CategoriaServicio
admin.site.register(CategoriaServicio)


