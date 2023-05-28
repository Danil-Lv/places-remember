from django import forms
from django.core.exceptions import ValidationError
from location_field.forms.plain import PlainLocationField

from .models import Place


class PlaceForm(forms.ModelForm):
    """Place"""
    location = PlainLocationField(based_fields=['title'],
                                  initial='55.85643, 37.99974',
                                  zoom=1)

    class Meta:
        model = Place
        fields = ['title', 'description', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2', 'rows': 5}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_location(self):
        try:
            location = self.cleaned_data['location'].split(',')
            lat = float(location[0])
            lng = float(location[1])
            assert -180 <= lng and -90 <= lat <= 90
            return self.cleaned_data['location']

        except:
            raise ValidationError('Неправильный формат координат')
