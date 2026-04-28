from django import forms
from .models import teacher
from .models import PDF

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class pdfr(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['PDF']



