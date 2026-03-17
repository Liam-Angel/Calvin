from django.contrib import admin

from .models import teacher
from .models import twin
from .models import student

admin.site.register(teacher)
admin.site.register(twin)
admin.site.register(student)