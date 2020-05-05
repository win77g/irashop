from django.db import models

# Create your models here.
class ClientModel(models.Model):
    lastname = models.CharField(max_length=120,blank=True, null=True, default=None,verbose_name="Фамилия")
    email = models.EmailField(blank=True, null=True, default=None)
    firstname = models.CharField(max_length=120,blank=True, null=True, default=None,verbose_name="Имя")
    phone = models.CharField(max_length=50, blank=True, null=True, default=None,verbose_name="Тел.")
    address = models.CharField(max_length=128, blank=True, null=True, default=None,verbose_name="Адрес")
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Созд.")
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name="Обнов.")
    token_key = models.CharField(max_length=128,blank=True, null=True, default=None)
    # вывод одного поля
    def __str__(self):
        return "Клиент %s " % (self.id )
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
