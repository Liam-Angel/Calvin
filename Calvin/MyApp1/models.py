from django.db import models



# Create your models here.
class twin(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class teacher(models.Model):
    Name = models.CharField(max_length=25, blank=True)
    Area = models.CharField(max_length=30, blank=True)
    

class student(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class fileModel(models.Model):
    Title = models.CharField(max_length=25, blank=True)
    File = models.FileField(upload_to='H:/Programming/Calvin/Calvin/MyApp1/files', blank=True)

class PDF(models.Model):
    PDF = models.CharField(max_length=25, blank=True)
    