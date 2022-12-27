from django import forms
from django.forms import ModelForm
from .models import Work, WorkComment


class WorkForm(ModelForm):
    class Meta:
        model = Work

        fields = ('title', 'team', 'date_due', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'date_due': forms.DateInput(attrs={'class': 'form-control', "type":"date"}),
            'team': forms.Select(attrs={'class': 'form-control', 'placeholder': 'team'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }


class WorkCommentForm(ModelForm):
    class Meta:
        model = WorkComment

        fields = ('description',)

        labels = {
            'description': '',
        }

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'new comment','rows': 2}),
        }