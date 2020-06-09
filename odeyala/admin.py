from django.contrib import admin
from .models import *
# from metatags.admin import MetaTagInline
# from properties.models import CategoryProperty, ProductProperty
# from filters.models import FilterCategory, ProductFilter, FilterSelect
from django.forms import TextInput, ModelForm, Textarea, Select

# Register your models here.


# ----------------------------Brend--------------------------------------------------------------
class BrendAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Brend._meta.fields]

      class Meta:
           model = Brend
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
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
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Tkan, TkanAdmin)
# ----------------------------END Tkan--------------------------------------------------------------
# ----------------------------Size------------------------------------------------------------------
class SizeAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Size._meta.fields]

      class Meta:
           model = Size
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Size, SizeAdmin)
# ----------------------------END Size--------------------------------------------------------------
# ----------------------------Type------------------------------------------------------------------
class TypeAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Type._meta.fields]

      class Meta:
           model = Type
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Type, TypeAdmin)
# # ----------------------------END Type--------------------------------------------------------------
# ----------------------------Filler------------------------------------------------------------------
class FillerAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Filler._meta.fields]

      class Meta:
           model = Filler
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Filler, FillerAdmin)
# ----------------------------END Filler--------------------------------------------------------------
# ----------------------------FillerWeight------------------------------------------------------------------
class FillerWeightAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in FillerWeight._meta.fields]

      class Meta:
           model = FillerWeight
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(FillerWeight, FillerWeightAdmin)
# ----------------------------END FillerWeight-------------------------------------------------------------

# ----------------------------Gallery---------------------------------------------------------------
#добавление фоток внизу прдукт админки
class OdeyalaImageInline(admin.TabularInline):
    model = OdeyalaImage
    extra = 1
    list_display = ['image_img',]
    readonly_fields = ['image_img',]
# ---------------------------- end Gallery----------------------------------------------------------

# ----------------------------Product----------------------------------------------------------
# Register your models here.
class OdeyalaAdmin (admin.ModelAdmin):

   inlines = [OdeyalaImageInline,]
   list_display = ('name','brend','image_img', 'price','is_active','new_product','top','slider')
   readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["price","name","brend__name"]
   list_filter = ['brend','is_active','new_product','top']

   list_per_page = 15


class Meta:
    model = Odeyala
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Odeyala,OdeyalaAdmin)
