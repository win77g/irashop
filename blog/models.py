from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.db.models.signals import  pre_save
from transliterate import translit
# преврашает в slug
from django.utils.text import slugify

class Teg(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит',unique=True,)
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Teg)
# создание названия фотки
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)

class Blog(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    category = models.ForeignKey(Teg, blank=True, null=True,related_name = 'cat',on_delete=models.CASCADE,verbose_name='Категория',to_field='slug')
    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка')
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    key_word = models.CharField(verbose_name='Ключевые слова',max_length=120,blank=True, null=True )
    key_description = models.CharField(verbose_name='Мето описани',max_length=120,blank=True, null=True )
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)
    description_short = RichTextUploadingField(verbose_name='Текст(короткий)',blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True,verbose_name='В наличии')
    top = models.BooleanField(default=False,verbose_name='В топе(на гл.странице)')
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Дата последнего обновления')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статья'


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
pre_save.connect(pre_save_product_slug, sender=Blog)
