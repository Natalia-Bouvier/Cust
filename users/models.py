from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from  empresa.models import Empresa

class ManejadorUsuario(BaseUserManager):
    def create_user(self, correo, password=None):
        if not correo:
            raise ValueError('Usuarios deben tener un correo electronico valido.')
        usuario = self.model(
            correo=self.normalize_email(correo),
        )
        usuario.user
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_staffuser(self, correo, password):
        usuario = self.create_user(
            correo, 
            password=password,
        )
        usuario.staff=True
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password):
        usuario=self.create_user(
            correo,
            password=password,
        )
        usuario.staff=True
        usuario.admin=True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    Nombre = models.CharField(max_length=35, default="")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200,default='Dirección del cliente')
    sexo = (('Femenino','Femenino'),('Masculino','Masculino'),)
    sexo = models.CharField(max_length = 10, choices = sexo)
    telefono = models.CharField(max_length=9,default='Teléfono del cliente')
    correo = models.EmailField(verbose_name='correo electronico' , max_length=255 , unique=True, default="")
    cedula = models.CharField(max_length=15,default='1.111.111-1')
    Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, null=True)
    Observaciones = models.CharField(max_length=1000, default="")

    active = models.BooleanField(('activo'), default=True)
    staff=models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    groups = models.IntegerField(default=0)
    user_permissions = models.IntegerField(default=0)
    objects = ManejadorUsuario()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('usuario')
        verbose_name_plural = ('usuarios')
    def get_name(self):
        return self.Nombre
    def has_perm(self, perm, obj=None):
        "El usuario cuenta con un permiso en especifico?"
        return True
    def has_module_perms(self, app_label):
        "El usuario cueta con los permisos para ver una app en especifico?"
        return True
    
    @property
    def is_staff(self):
        "El usuario es Colaborador"
        return self.staff
    @property
    def is_admin(self):
        "El usuario es un administrador?"
        return self.admin
    @property
    def is_active(self):
        "El usuario esta activo?"
        return self.active

    def __str__(self):
       return self.Nombre 


