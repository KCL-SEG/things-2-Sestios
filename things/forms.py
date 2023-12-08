"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
    
    widgets = {
        'description': forms.Textarea(attrs={'maxlength': 120}),
    }

    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)