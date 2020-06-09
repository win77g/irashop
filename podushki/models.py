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
# ------------------------------------модель Ткань---------------------------------------------------
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
# ----------------------------------модель Size------------------------------------------------------
class Size(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размер'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Size)
# ----------------------------------end Ткань------------------------------------------------
# ---------------------------------Type -----------------------------------------------------
class Type(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Тип одеяла'
        verbose_name_plural = 'Тип одеяла'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Type)
# ---------------------------------Type end--------------------------------------------------
# ---------------------------------filler наполнитель----------------------------------------
class Filler(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Наполнитель'
        verbose_name_plural = 'Наполнитель'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Filler)
# ---------------------------------filler наполнитель end----------------------------------------

# ----------------------------------Product-------------------------------------------------------
# создание названия фотки
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)


# модеь продукта
class Podushki(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    brend = models.ForeignKey(Brend,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Бренд',to_field='name')
    tkan = models.ForeignKey(Tkan,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Ткань',to_field='name')
    size = models.ForeignKey(Size,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Размер',to_field='name')
    type = models.ForeignKey(Type,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Тип',to_field='name')
    filler = models.ForeignKey(Filler,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Наполнитель',to_field='name')
    key_words = models.CharField(verbose_name='Ключи',max_length=120,blank=True, null=True )
    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка')
    image_link = models.CharField(verbose_name='Фотка ссылка',max_length=120,blank=True, null=True )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена ')
    price_old = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Старая цена ')
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)
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
        verbose_name = 'Подушки'
        verbose_name_plural = 'Подушки'


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
pre_save.connect(pre_save_product_slug, sender=Podushki)
# -----------------------------end product-------------------------------------------------------------
#  --------------------------Gallery-------------------------------------------------------
# создание названия фотки
def image_gallary_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# фотки продукта
class PodushkiImage(models.Model):
    product = models.ForeignKey(Podushki,blank=True, null=True, default=None,on_delete=models.CASCADE)
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
pre_save.connect(pre_save_imagegallery_slug, sender=PodushkiImage)
# ---------------------------------------end gallery-------------------------------------------

