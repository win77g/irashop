from django.contrib import admin
from .models import *
# from metatags.admin import MetaTagInline
# from properties.models import CategoryProperty, ProductProperty
# from filters.models import FilterCategory, ProductFilter, FilterSelect
from django.forms import TextInput, ModelForm, Textarea, Select

# Register your models here.
# ----------------------------Category----------------------------------------------------------
class CategoryAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Category._meta.fields]
      # add meatateg fields
      # inlines = (MetaTagInline,)
      class Meta:
           model = Category
      def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Category, CategoryAdmin)


# class ProductCategoryAdmin (admin.ModelAdmin):
#    #  вывод всех полей в админку
#       list_display = [field.name for field in ProductCategory._meta.fields]
#
#       class Meta:
#            model = ProductCategory
# # Register your models here.
# admin.site.register(ProductCategory, ProductCategoryAdmin)
# ----------------------------END Category----------------------------------------------------------

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

# ----------------------------Gallery----------------------------------------------------------
#добавление фоток внизу прдукт админки
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    list_display = ['image_img',]
    readonly_fields = ['image_img',]
# ---------------------------- end Gallery----------------------------------------------------------

# ----------------------------Product----------------------------------------------------------
# Register your models here.
class ProductAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   inlines = [ProductImageInline,]
   list_display = ('name','brend','categ','image_img', 'price_polutorca','is_active','new_product','top','slider')
   readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["price","name","brend__name"]
   list_filter = ['categ','brend','is_active','new_product','top']
   # suit_form_tabs = (
   #      ('main', 'Main'),
   #      ('params', 'Params'),
   #      ('filters','Filters'),)
   # fieldsets = [('Main',{
   #                   'classes': ('suit-tab', 'suit-tab-main',),
   #                   'fields':[
   #         'name','brend','categ','attributes','description','description_short','image_img', 'price','is_active','new_product','top','slider'
   #                   ]
   #                       }
   #               )]
   list_per_page = 15

   # ------------


   # meta

   # inlines = (MetaTagInline,)

   # def formfield_for_manytomany(self, db_field, request=None, **kwargs):
   #      if db_field.name == 'membership':
   #          qs = kwargs.get('queryset', db_field.remote_field.model.objects)
   #          # Avoid a major performance hit resolving membership names which
   #          # triggers a content_type load:
   #          kwargs['queryset'] = qs.select_related('content_type')
   #      return super().formfield_for_manytomany(db_field, request=request, **kwargs)
   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = Product
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(Product,ProductAdmin)
# ----------------------------END Product----------------------------------------------------------
