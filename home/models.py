from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import  pre_save
# преврашает в slug
from django.utils.text import slugify
# переводит кирилицу в латынь
from transliterate import translit

#  ---------------------------------------Gallery-------------------------------------------------------
# создание названия фотки
def image_gallary_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# фотки продукта
class BigSliderImageModel(models.Model):
    category = models.CharField(verbose_name='Название категории',max_length=120,blank=True, null=True ,unique=True)
    lozung = models.CharField(verbose_name='Рекламный текст',max_length=120,blank=True, null=True)
    brendi = models.CharField(verbose_name='Торг.марки',max_length=120,blank=True, null=True)
    image = models.ImageField(upload_to= image_gallary_folder,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None , verbose_name='Транслит')
    is_active = models.BooleanField(default=True)


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
pre_save.connect(pre_save_imagegallery_slug, sender = BigSliderImageModel)
# ------------------------------------------end gallery--------------------------------------------------


# фотки продукта
class AdvertisingImageModel(models.Model):
    image = models.ImageField(upload_to= image_gallary_folder,blank=True, null=True, default=None)
    text = models.CharField(max_length=120,blank=True, null=True, default=None , verbose_name='Текст1')
    text2 = models.CharField(max_length=120,blank=True, null=True, default=None , verbose_name='Текст2')
    link = models.CharField(max_length=120,blank=True, null=True, default=None , verbose_name='ссылка')
    slug = models.SlugField(blank=True, null=True, default=None , verbose_name='Транслит')
    is_active = models.BooleanField(default=True)


    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

# автоматическое сохранение поля слаг в gallery
# def pre_save_imagegallery_slug(sender,instance, *args, **kwargs):
#     # print(instance.filename)
#     if not instance.slug:
#         slug = slugify(translit(instance.product.name, reversed=True))
#         instance.slug = slug
# pre_save.connect(pre_save_imagegallery_slug, sender = BigSliderImageModel)
# ---------------------------------------end gallery----------------------------------
