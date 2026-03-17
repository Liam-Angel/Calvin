from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .models import twin
from .models import student
from .forms import InputForm

# Create your views here.
def index(request):
   twins = twin.objects.all
   teachers = teacher.objects.all
   students = student.objects.all
   return render(request,"MyApp1/index.html",{'content2': twins, 'content': teachers, 'content3': students})

def input_view(request):
    if 'submit' in request.POST:
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()

    if 'back' in request.POST:
        return redirect("index")

    else:
     form = InputForm()
    return render(request, "MyApp1/input.html", {"form": form})
    

