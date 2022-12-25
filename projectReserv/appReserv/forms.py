from .models import Compagnie
from django import forms


class CompagnieForm(forms.ModelForm):
    class Meta:
        model=Compagnie
        fields = ('nom','logo')
