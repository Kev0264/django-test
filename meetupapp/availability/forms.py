from django import forms
from .models import GeneralAvailability, AvailabilityOverride

class GeneralAvailabilityForm(forms.ModelForm):
    class Meta:
        model = GeneralAvailability
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        widgets = {
            'monday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Monday availability'}),
            'tuesday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tuesday availability'}),
            'wednesday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wednesday availability'}),
            'thursday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Thursday availability'}),
            'friday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Friday availability'}),
            'saturday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saturday availability'}),
            'sunday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sunday availability'}),
        }
        labels = {
            'monday': 'Monday',
            'tuesday': 'Tuesday',
            'wednesday': 'Wednesday',
            'thursday': 'Thursday',
            'friday': 'Friday',
            'saturday': 'Saturday',
            'sunday': 'Sunday',
        }

class AvailabilityOverrideForm(forms.ModelForm):
    class Meta:
        model = AvailabilityOverride
        fields = ['date', 'is_available']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'date': 'Date',
            'is_available': 'Available?'
        }