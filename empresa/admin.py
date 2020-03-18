from django.contrib import admin

from .models import Empresa
admin.site.register(Empresa)

from .models import Colaborador
admin.site.register(Colaborador)


