from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from pypdf import PdfReader
from .models import teacher
from .models import twin
from .models import PDF
from .forms import InputForm
from .forms import pdfr


removals = []


# Create your views here.
def index(request):
   teachers = teacher.objects.all
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


def pdfr_view(request):
    PDFs = PDF.objects.all

    if 'submit' in request.POST:
        reader = PdfReader("meth.pdf")
        page = reader.pages[0]
        print(page.extract_text())
             
    if 'back' in request.POST:
        return redirect("index")
    else:

        return render(request, "MyApp1/pdfr.html",{})

