from django.contrib import admin

# Register your models here.
from .models import Student
class stud(admin.ModelAdmin):
    list_display=['id','name','roll','city']

admin.site.register(Student,stud)
