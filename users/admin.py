from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AdminFormaCreacionUsuario, AdminFormaActualizar
from .models import Usuario

class UserAdmin(BaseUserAdmin):
    form=AdminFormaActualizar
    add_form=AdminFormaCreacionUsuario

    list_display=('correo', 'admin')
    list_filter=('admin',)

    fieldsets=(
    (None,{'fields':('correo','password')}),
    ('Informacion Personal',{'fields':('Nombre','fecha_nacimiento','direccion','sexo','telefono','cedula','Empresa','Observaciones')}),
    ('Permisos Django',{'fields':('admin','staff','active','groups', 'user_permissions')}),
    )
    
    add_fieldsets=(
        (None,{
            'classes': ('wide',),
            'fields': ('correo', 'password1', 'password2')}
        ),
    )
    
    form = AdminFormaActualizar
    add_form = AdminFormaCreacionUsuario 
    ordering = ('correo',)   
    filter_horizontal = ()

admin.site.register(Usuario, UserAdmin)
