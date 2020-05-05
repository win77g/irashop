from django.db import models

class QuethenModel(models.Model):
    name = models.CharField(max_length=24,blank=True, null=True, default=None)
    phone = models.CharField(max_length=24,blank=True, null=True, default=None)
    email = models.CharField(max_length=24,blank=True, null=True, default=None)
    message = models.CharField(max_length=24,blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    # вывод одного поля
    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

