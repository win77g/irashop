from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# ----------------------------------STATUS--------------------------------------------------------------
class Status(models.Model):
    name = models.CharField(max_length=24,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    # вывод одного поля
    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'
# ----------------------------------PRODUCT IN BASKET----------------------------------------------------------
class  ProductInBasketModel(models.Model):
    token_key = models.CharField(max_length=128,blank=True, null=True, default=None)
    qty = models.IntegerField(default=1,blank=True, null=True,verbose_name='Кол.во')
    size = models.CharField(max_length=10,blank=True, null=True, default=None,verbose_name='Размер')
    product = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Продукт')
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Цена',null=True)
    image = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Фото')
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Итого',null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Обновлён')

    # # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id)
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    # def save(self, *args, **kwargs):
    #     price_per_item = self.product.price
    #     self.price_per_item = price_per_item
    #     self.total_price = int(self.nmb) * self.price_per_item
    #
    #     super(ProductInBasket, self).save(*args, **kwargs)
# ----------------------------------END PRODUCT IN ORDRE----------------------------------------------------------
class OrderModel(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, default=None,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0)#total price for all products in order
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_surname = models.CharField(max_length=120,blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=120,blank=True, null=True, default=None)
    customer_tel = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    token = models.CharField(max_length=128,blank=True, null=True, default=None)
    # productinorder = models.ForeignKey(ProductInOrder, blank=True, null=True, default=None)
    # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id )
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ProductInOrderModel(models.Model):
    order = models.ForeignKey(OrderModel,blank=True, null=True, default=None,on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, blank=True, null=True, default=None,on_delete=models.CASCADE,to_field="name")
    product = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Продукт')
    nmb = models.IntegerField(default=1)
    size = models.CharField(max_length=10,blank=True, null=True, default=None,verbose_name='Размер')
    price_per_item = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    image = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Фото')
    total_price = models.DecimalField(max_digits=10,decimal_places=2, default=0)#price*nmb
    # customer_email = models.EmailField(blank=True, null=True, default=None)
    # customer_name = models.CharField(max_length=120,blank=True, null=True, default=None)
    # customer_tel = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    # # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id)
    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        # price = self.price_per_item
        # self.price = price
        # self.total_price = int(self.qty) * self.price

        order = self.order

        all_product_in_order = ProductInOrderModel.objects.filter(order=order, is_active=True)

        order_total_price = 0
        for item in all_product_in_order:
            order_total_price = order_total_price + item.total_price

        self.order.total_price =order_total_price
        self.order.save(force_update=True)
        super(ProductInOrderModel, self).save(*args, **kwargs)
def product_in_order_post_save(sender,instance,created,**kwargs):
   order = instance.order
   all_product_in_order = ProductInOrderModel.objects.filter(order=order, is_active=True)

   order_total_price = 0
   for item in all_product_in_order:
     order_total_price += item.total_price

   instance.order.total_price = order_total_price
   instance.order.save(force_update=True)
post_save.connect(product_in_order_post_save, sender = ProductInOrderModel)
