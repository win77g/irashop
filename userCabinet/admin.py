from django.contrib import admin
from .models import *

class ClientModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Order._meta.fields]
      list_display = ('lastname','email','firstname','phone','address',
                  'created','updated',
                  'token_key',)
      # list_filter = ['status']
      search_fields = ['email','phone']


      # actions = [make_do]
class Meta:
    model = ClientModel
# Register your models here.
admin.site.register(ClientModel,ClientModelAdmin)
