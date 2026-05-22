from django import forms
from django.forms import inlineformset_factory
from .models import teacher
from .models import units
from .models import tasks
from .models import PDF


class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class UnitForm(forms.ModelForm):
    class Meta:
        model = units
        fields = ['Class', 'Unit', 'Description', 'AdditionalInfo']

class TaskForm(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['Task', 'DueDate', 'Weight', 'Unit']

TaskFormSet = inlineformset_factory(
    units,
    tasks,
    fields=['Task', 'DueDate', 'Weight', 'Unit'],
    extra=5, # how many extra forms in the formset
    can_delete=True
)


class pdfr(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['PDF']

#TaskFormSet = inlineformset_factory(units, tasks, fields=['Task', 'DueDate', 'Weight'], extra=2)

