from django.urls import include, re_path
import MyApp1.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    re_path(r'^$', MyApp1.views.index, name='index'),
    re_path(r'^home$', MyApp1.views.index, name='index'),
    re_path(r'input', MyApp1.views.input_view, name='input'),
    re_path(r'pdfr', MyApp1.views.pdfr_view, name='pdfr'),
    path('fileUpload/<int:pk>/', MyApp1.views.fileUpload_view, name='fileUpload'),
    re_path(r'addUnit', MyApp1.views.addUnit_view, name='addUnit'),
    path('report/', MyApp1.views.report, name='report'),

]
