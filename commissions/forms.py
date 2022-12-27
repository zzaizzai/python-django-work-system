from django import forms
from django.forms import ModelForm
from .models import Commission, CommissionComment


class CommissionForm(ModelForm):
    class Meta:
        model = Commission

        fields = ('title', 'team', 'date_due', 'description', 'is_cancled')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'date_due': forms.DateInput(attrs={'class': 'form-control', "type":"date"}),
            'team': forms.Select(attrs={'class': 'form-control', 'placeholder': 'team'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }


class CommissionCommentForm(ModelForm):
    class Meta:
        model = CommissionComment

        fields = ('description',)

        labels = {
            'description': '',
        }

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'new comment','rows': 2}),
        }
