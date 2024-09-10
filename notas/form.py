from django import forms
from .models import notas


class formulario(forms.ModelForm):
    class Meta:
        model = notas
        fields = '__all__'

