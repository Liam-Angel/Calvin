from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from pypdf import PdfReader
from pypdf import PdfWriter
from reportlab.pdfgen import canvas
from .models import teacher, twin, PDF, units, tasks
from .forms import InputForm, pdfr, UnitForm, TaskFormSet
from reportlab.platypus import Paragraph,Image,Table 
from django.http import FileResponse 
from django.contrib.staticfiles.storage import staticfiles_storage 
from io import BytesIO


removals = []
removals2 = []


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

    selected = teacher.objects.filter(id__in=removals)    
    
    if 'delete' in request.POST:
        for item in removals:
            if teacher.objects.filter(id=item).exists():
                entry = teacher.objects.get(id=item)
                entry.delete()
                removals.clear

    if 'back' in request.POST:
        removals.clear
        return redirect("index")
    else:
        form = InputForm()
        return render(request, "MyApp1/input.html",{'form': form, 'content': teachers, 'removals': removals, 'selected': selected})


def pdfr_view(request):
    PDFs = PDF.objects.all
    page
    if 'submit' in request.POST:
        reader = PdfReader("H:\Programming\Calvin\Calvin\MyApp1\math.pdf")
        page = reader.pages[0]
        print(page.extract_text())
             
    if 'back' in request.POST:
        return redirect("index")
    else:

        return render(request, "MyApp1/pdfr.html",{'page',page.extract_text() })


def generate_pdf_file():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]
    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def report(request):
    pdf_file =  staticfiles_storage.path("meth.pdf")

    try:
        merger = PdfWriter()
        input1 = PdfReader(generate_pdf_file())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)
        response = FileResponse(buffer, as_attachment=True, filename="hello.pdf")

    except FileNotFoundError:

        response = FileResponse(generate_pdf_file(), as_attachment=True, filename="no.pdf")

    return response

def fileUpload_view(request):
   unit = units.objects.all
   task = tasks.objects.all


   if 'save' in request.POST:
      form = UnitForm(request.POST)
      if form.is_valid():
          print('saving')
          form.save()

   if 'save2' in request.POST:
      formset = TaskFormSet(request.POST)
      if formset.is_valid():
          print('saving')
          formset.save()
      

   if 'delete' in request.POST:
       id = request.POST.get("delete")
       if units.objects.filter(id=id).exists():
           entry = units.objects.get(id=id)
           entry.delete()

   if 'back' in request.POST:
       removals2.clear
       return redirect("index")
   else:
       form = UnitForm()
       formset = TaskFormSet()
       return render(request, "myapp1/fileupload.html",{'form': form, 'formset': formset, 'unit': unit, 'task': task,})
