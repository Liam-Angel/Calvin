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


class tasks(models.Model):
    Unit = models.CharField(max_length=25, blank=True)
    Task = models.CharField(max_length=25, blank=True)
    DueDate = models.CharField(max_length=25, blank=True)
    Weight = models.CharField(max_length=25, blank=True)


class units(models.Model):
    Class = models.CharField(max_length=25, blank=True)
    Unit = models.CharField(max_length=25, blank=True)
    Description = models.CharField(max_length=25, blank=True)
    Assessment = models.ManyToManyField(tasks, blank=True)
    AdditionalInfo = models.FileField(upload_to='C:/Users/LiamA/source/repos/Liam-Angel/Calvin/Calvin/MyApp1/files/', blank=True)


class PDF(models.Model):
    PDF = models.CharField(max_length=25, blank=True)
    