from django import forms
from django.forms import ModelForm
from .models import Work


class WorkForm(ModelForm):
    class Meta:
        model = Work

        fields = ('title', 'team', 'date_due', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'date_due': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'date_due'}),
            'team': forms.Select(attrs={'class': 'form-control', 'placeholder': 'team'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
