from django.contrib import admin
from .models import *
# Register your models here.
class Bookadmin(admin.ModelAdmin):
    list_display=['title','author','pdf']
admin.site.register(Book,Bookadmin)