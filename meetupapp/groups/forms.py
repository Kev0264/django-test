from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'meeting_time', 'interests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Group description'}),
            'meeting_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meeting time'}),
            'interests': forms.Textarea(attrs={'rows': 3})
        }
        labels = {
            'name': 'Group name',
            'description': 'Description',
            'meeting_time': 'Meeting time',
            'interests': 'Interests'
        }