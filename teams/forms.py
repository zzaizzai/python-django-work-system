from django import forms
from django.forms import ModelForm
from .models import Team, Member_Team


# class TeamMemberForm(ModelForm):
#     class Meta:
#         model = Member_Team

#         field = ('name')

#         widgets = {
#             'name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'new comment','rows': 2}),
#         }