from django import forms
from .models import Empresa

class FormaRegistroEmpresa(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ('correo', 'Nombre', 'razon_social', 'direccion', 'rut', 'telefono')

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        qs = Empresa.objects.filter(rut=rut)
        if qs.exists():
            raise forms.ValidationError("empresa ya registrada")
        return rut