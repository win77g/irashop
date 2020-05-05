from django.contrib import admin
from .models import *
class WishlistModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in WishlistModel._meta.fields]

class Meta:
    model = WishlistModel
# Register your models here.
admin.site.register(WishlistModel,WishlistModelAdmin)
