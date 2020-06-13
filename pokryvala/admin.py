from django.contrib import admin
from .models import *
# Register your models here.

# ----------------------------Brend--------------------------------------------------------------
class BrendAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Brend._meta.fields]

      class Meta:
           model = Brend
      def get_prepopulated_fields(self, request, obj=None):

        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Brend, BrendAdmin)
# ----------------------------END Brend--------------------------------------------------------------
# ----------------------------Tkan--------------------------------------------------------------
class TkanAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Tkan._meta.fields]

      class Meta:
           model = Tkan
      def get_prepopulated_fields(self, request, obj=None):

        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Tkan, TkanAdmin)
# ----------------------------END Tkan--------------------------------------------------------------
# ----------------------------Size--------------------------------------------------------------
class SizeAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Size._meta.fields]

      class Meta:
           model = Size
      def get_prepopulated_fields(self, request, obj=None):

        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Size, SizeAdmin)
# ----------------------------END Size--------------------------------------------------------------
# ----------------------------Dekor--------------------------------------------------------------
class DekorAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Dekor._meta.fields]

      class Meta:
           model = Dekor
      def get_prepopulated_fields(self, request, obj=None):

        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Dekor, DekorAdmin)
# ----------------------------END Dekor--------------------------------------------------------------
# ----------------------------Gallery---------------------------------------------------------------
#добавление фоток внизу прдукт админки
class PokryvalaImageInline(admin.TabularInline):
    model = PokryvalaImage
    extra = 1
    list_display = ['image_img',]
    readonly_fields = ['image_img',]
# ---------------------------- end Gallery----------------------------------------------------------

# ----------------------------Product----------------------------------------------------------
# Register your models here.
class PokryvalaAdmin (admin.ModelAdmin):

   inlines = [PokryvalaImageInline,]
   list_display = ('name','brend','image_img', 'price','is_active','new_product','top','slider')
   readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["price","name","brend__name"]
   list_filter = ['brend','is_active','new_product','top']

   list_per_page = 15


class Meta:
    model = Pokryvala
    def get_prepopulated_fields(self, request, obj=None):

        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Pokryvala,PokryvalaAdmin)
