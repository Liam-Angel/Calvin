from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .models import twin

# Create your views here.
def index(request):
   twins = twin.objects.all
   return render(request,"MyApp1/index.html",{'content': twins})

def index(request):
   teachers = teacher.objects.all
   return render(request,"MyApp1/index.html",{'content': teachers})
 
