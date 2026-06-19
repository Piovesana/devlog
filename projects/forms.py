from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['titulo', 'descricao']


    widgets = {
        'titulo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Aprender React'}),
        'descricao': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Descreva o objetivo do projeto...'}),
        }