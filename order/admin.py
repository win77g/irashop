from django.contrib import admin
from .models import *

# добавить действие в окно выполнить действие
def make_payed(modeladmin,request,queryset):
    queryset.update (status=3)
make_payed.short_description = "Пометить как оплаченные"

def make_do(modeladmin,request,queryset):
    queryset.update (status=2)
make_do.short_description = "Пометить как выполнен"

def make_new(modeladmin,request,queryset):
    queryset.update (status=4)
make_new.short_description = "Пометить как обновленный"

class StatusAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Status._meta.fields]

class Meta:
    model = Status
# Register your models here.
admin.site.register(Status,StatusAdmin)

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrderModel
    extra = 0

# product in basket
class ProductInBasketAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in ProductInBasketModel._meta.fields]

class Meta:
    model = ProductInBasketModel
# Register your models here.
admin.site.register(ProductInBasketModel,ProductInBasketAdmin)

class OrderModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Order._meta.fields]
      list_display = ('id','status','total_price','customer_surname','customer_name','customer_email','customer_tel','customer_address','token','comments','created')
      # list_filter = ['status']
      # search_fields = ["id","total_price"]
      inlines = [ProductInOrderInline]
      actions = [make_payed,make_do,make_new]

      # actions = [make_do]
class Meta:
    model = OrderModel
# Register your models here.
admin.site.register(OrderModel,OrderModelAdmin)

class ProductInOrderModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in ProductInOrderModel._meta.fields]

class Meta:
    model = ProductInOrderModel
# Register your models here.
admin.site.register(ProductInOrderModel,ProductInOrderModelAdmin)
