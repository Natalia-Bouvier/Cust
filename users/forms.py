from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario

#Crear un superUsuario en consola
class FormaRegistro(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('correo','Nombre','fecha_nacimiento','direccion','sexo','telefono','cedula','Observaciones','active','staff', 'admin')

    def clean_email(self):
        correo = self.cleaned_data.get('correo')
        qs = Usuario.objects.filter(correo=correo)
        if qs.exists():
            raise forms.ValidationError("correo ya registrado")
        return correo
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

#Crear un Usuario en consola
class AdminFormaCreacionUsuario(forms.ModelForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('correo','Nombre','fecha_nacimiento','direccion','sexo','telefono','cedula','Observaciones','active','staff', 'admin')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        usuario=super(AdminFormaCreacionUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data.get("password1"))
        usuario.active = True
        usuario.staff = True
        usuario.admin = True
        if commit:
            usuario.save()
        return usuario

class AdminFormaActualizar(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=Usuario
        fields=('correo', 'password','Nombre', 'fecha_nacimiento', 'direccion', 'sexo', 'telefono', 'cedula', 'Empresa', 'Observaciones', 'active', 'admin')

    def clean_password(self):
        return self.initial['password']


