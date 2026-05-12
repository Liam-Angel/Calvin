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
    Title = models.CharField(max_length=25)
    File = models.FileField(upload_to=None, max_length=254)

class PDF(models.Model):
    PDF = models.CharField(max_length=25, blank=True)
    