from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .models import twin
from .models import student
from .forms import InputForm

removals = []


# Create your views here.
def index(request):
   twins = twin.objects.all
   teachers = teacher.objects.all
   students = student.objects.all
   return render(request,"MyApp1/index.html",{'content': teachers})

def input_view(request):
    teachers = teacher.objects.all
   
    if 'submit' in request.POST:
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
    if 'select' in request.POST:
        id = request.POST.get("select")
        if teacher.objects.filter(id=id).exists():
            removals.append(id)
            
    if 'delete' in request.POST:
        for item in removals:
            if teacher.objects.filter(id=item).exists():
                entry = teacher.objects.get(id=item)
                entry.delete()
                removals.clear

            

    if 'back' in request.POST:
        return redirect("index")
    else:
        form = InputForm()
        return render(request, "MyApp1/input.html",{'form': form, 'content': teachers, 'removals': removals})

