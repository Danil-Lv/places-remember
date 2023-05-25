from django import forms
from location_field.forms.plain import PlainLocationField

from .models import Place


class PlaceForm(forms.ModelForm):
    location = PlainLocationField(based_fields=['title'],
                                  initial='55.85643, 37.99974',
                                  zoom=1)

    class Meta:
        model = Place
        fields = ['title', 'description', 'location']
