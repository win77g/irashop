from django.contrib import admin
from .models import *

class BlogAdmin (admin.ModelAdmin):

   list_display = ('name','category','image_img','key_word','is_active','top','created','updated')
   readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["category","name",]
   list_filter = ["category","name",]
   list_per_page = 15


class Meta:
    model = Blog
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Blog,BlogAdmin)

class TegAdmin (admin.ModelAdmin):

   list_display = ('name','slug')

class Meta:
    model = Teg
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Teg,TegAdmin)
