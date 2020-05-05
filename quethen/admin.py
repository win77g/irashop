from django.contrib import admin
from .models import *
class QuethenModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in QuethenModel._meta.fields]

class Meta:
    model = QuethenModel
# Register your models here.
admin.site.register(QuethenModel,QuethenModelAdmin)
