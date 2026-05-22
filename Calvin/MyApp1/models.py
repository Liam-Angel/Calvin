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


class units(models.Model): #unit model
    Class = models.CharField(max_length=25, blank=True)
    Unit = models.CharField(max_length=25, blank=True) #unit name
    Description = models.CharField(max_length=25, blank=True) #unit description
    AdditionalInfo = models.FileField(upload_to="C:/Users/LiamA/source/repos/Liam-Angel/CalvinCalvin/MyApp1/files/", blank=True) #holds pdf file

class tasks(models.Model): #assessment model
    Unit = models.ForeignKey(units, on_delete=models.CASCADE)
    Task = models.CharField(max_length=25, blank=True)
    DueDate = models.CharField(max_length=25, blank=True)
    Weight = models.CharField(max_length=25, blank=True)


class PDF(models.Model):
    PDF = models.CharField(max_length=25, blank=True)
    