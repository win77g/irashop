from django.db import models
# from properties.models import ProductProperty, CategoryProperty
# from filters.models import ProductFilter, FilterCategory
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import  pre_save
# преврашает в slug
from django.utils.text import slugify
# переводит кирилицу в латынь
from transliterate import translit
from ckeditor_uploader.fields import RichTextUploadingField
import os
from django.dispatch import receiver

# model of Category
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True,)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',verbose_name="Родитель", db_index=True,on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='Транслит', null = True, unique=True,)
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)

    def __str__(self):
        return " %s" % self.name

    class MPTTMeta:
        order_insertion_by = ['name']

# ------------------------------модель Бренда---------------------------------------------------
class Brend(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Brend)
# ----------------------------------end brend--------------------------------------------------------
# ------------------------------модель Ткань---------------------------------------------------
class Tkan(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Ткань'
        verbose_name_plural = 'Ткань'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Tkan)
# ----------------------------------end Ткань--------------------------------------------------------
# ---------------------------------Product---------------------------------------------------
# создание названия фотки
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)


# модеь продукта
class Product(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    brend = models.ForeignKey(Brend,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Бренд',to_field='name')
    categ = TreeForeignKey(Category, blank=True, null=True,related_name = 'cat',on_delete=models.CASCADE,verbose_name='Категория',to_field='slug')
    key_words = models.CharField(verbose_name='Ключи',max_length=120,blank=True, null=True )
    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка')
    image_link = models.CharField(verbose_name='Фотка ссылка',max_length=120,blank=True, null=True )
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    tkan = models.ForeignKey(Tkan,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Ткань',to_field='name')
    price_polutorca = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена полуторка')
    price_old_polutorca = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Старая цена полуторка')
    price_dvuspal = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена двухспального')
    price_old_dvuspal = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Старая цена двухспального')
    price_semeuka = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена семейка')
    price_old_semeuka = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Старая цена семейки')
    price_euro = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена evro')
    price_old_euro = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Старая цена evro')
    # description = RichTextUploadingField(config_name='default')
    # description_short = RichTextUploadingField(config_name='default')
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)
    size_map = RichTextUploadingField(verbose_name='Карта размеров',blank=True, null=True, default=None)
    description_short = RichTextUploadingField(verbose_name='Текст(короткий)',blank=True, null=True, default=None)
    discount = models.IntegerField(default=0,verbose_name='Скидка')
    is_active = models.BooleanField(default=True,verbose_name='В наличии')
    new_product = models.BooleanField(default=False,verbose_name='Новинка')
    top = models.BooleanField(default=False,verbose_name='В топе(на гл.странице)')
    slider = models.BooleanField(default=False,verbose_name='Слайдер(на гл.странице)')
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Дата последнего обновления')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
# удаление фото

# автоматическое сохранение поля слаг в продуктах
def pre_save_product_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_product_slug, sender=Product)
# -----------------------------end product-------------------------------------------------------------
#  --------------------------Gallery-------------------------------------------------------
# создание названия фотки
def image_gallary_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# фотки продукта
class ProductImage(models.Model):
    product = models.ForeignKey(Product,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to= image_gallary_folder,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None , verbose_name='Транслит')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

# автоматическое сохранение поля слаг в gallery
def pre_save_imagegallery_slug(sender,instance, *args, **kwargs):
    # print(instance.filename)
    if not instance.slug:
        slug = slugify(translit(instance.product.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_imagegallery_slug, sender=ProductImage)
# ---------------------------------------end gallery----------------------------------
