from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'birth_date', 'passed_away_date', 'image']  
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'passed_away_date': forms.DateInput(attrs={'type': 'date'}),
        }
