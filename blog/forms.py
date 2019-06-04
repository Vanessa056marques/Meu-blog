from django import forms

from .models import Poat

class PoatForm(forms.ModelForm):
    class Meta:
        model = Poat
        fields = ('title', 'text')