from django import forms
from django.forms import ModelForm
from .models import Team, Member_Team


class TeamMemberForm(ModelForm):
    class Meta:
        model = Member_Team

        fields = ('member',)

        labels = {
            'member': '',
        }

        widgets = {
            'member': forms.Select(attrs={'class': 'form-control', 'placeholder': 'member'}),
        }