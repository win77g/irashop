from django.contrib import admin
from .models import *
# Простой вишлист для постельки
class WishlistModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in WishlistModel._meta.fields]

class Meta:
    model = WishlistModel
# Register your models here.
admin.site.register(WishlistModel,WishlistModelAdmin)

# Простой вишлист для детского постельного
class WishlistDpModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in WishlistDpModel._meta.fields]

class Meta:
    model = WishlistDpModel
# Register your models here.
admin.site.register(WishlistDpModel,WishlistDpModelAdmin)
