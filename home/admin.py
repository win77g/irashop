from django.contrib import admin
from .models import *

class BigSliderImageAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = ['category','lozung','brendi','image_img','slug','is_active']
      readonly_fields = ['image_img',]
      class Meta:
           model = BigSliderImageModel
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('category',)
        }
# Register your models here.
admin.site.register(BigSliderImageModel, BigSliderImageAdmin)

class AdvertisingImageModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = ['text','image_img','text2','link','slug','is_active']
      readonly_fields = ['image_img',]
      class Meta:
           model = AdvertisingImageModel
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('text',)
        }
# Register your models here.
admin.site.register(AdvertisingImageModel, AdvertisingImageModelAdmin)
