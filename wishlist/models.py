from django.db import models
from product.models import Product

# Create your models here.
class  WishlistModel(models.Model):
    token_key = models.CharField(max_length=128,blank=True, null=True, default=None)
    product_name = models.CharField(unique=True,max_length=128,blank=True, null=True, default=None,verbose_name='Продукт')
    slug = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Слаг')
    price_1 = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Цена 1,5')
    price_2 = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Цена 2')
    price_3 = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Цена семья')
    price_4 = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Цена Евро')
    image = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Фото')
    tkan = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Ткань')
    brend = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Бренд')
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Создан')


    # # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id)
    class Meta:
        verbose_name = 'Товар в жиланиях'
        verbose_name_plural = 'Товары в жиланиях'


class  WishlistDpModel(models.Model):
    token_key = models.CharField(max_length=128,blank=True, null=True, default=None)
    product_name = models.CharField(unique=True,max_length=128,blank=True, null=True, default=None,verbose_name='Продукт')
    size = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Размер')
    slug = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Слаг')
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0,verbose_name='Цена')
    image = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Фото')
    tkan = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Ткань')
    brend = models.CharField(max_length=128,blank=True, null=True, default=None,verbose_name='Бренд')
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Создан')


    # # вывод одного поля
    def __str__(self):
        return "Заказ %s " % (self.id)
    class Meta:
        verbose_name = 'Товар в жиланиях'
        verbose_name_plural = 'Товары в жиланиях'
