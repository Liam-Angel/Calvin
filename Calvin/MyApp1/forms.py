from django import forms
from .models import teacher
#from .models import fileModel
from .models import PDF

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

#class FileUploadForm(forms.ModelForm):
    #class Meta:
        #model = fileModel
        #fields = ['Title', 'File']

class pdfr(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['PDF']



