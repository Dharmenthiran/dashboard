# Board/forms.py
from django import forms
from .models import *

class MechineForm(forms.ModelForm):
    class Meta:
        model = Mechine
        fields = '__all__'
