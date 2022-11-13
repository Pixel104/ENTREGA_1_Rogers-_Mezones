from django import forms


class MascotaFormulario(forms.Form):
    nombre_mascota = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField(help_text="AAAA-MM-DD")


class CriadorFormulario(forms.Form):
    nombre_criador = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    provincia = forms.CharField(max_length=30)
    fecha_nacimiento = forms.DateField(help_text="AAAA-MM-DD")

class AlimentoFormulario(forms.Form):
    sabor = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    tamaño = forms.CharField(max_length=20, help_text="1/2 Kilo, 1 kilo, 4 Kilo, etc")

