# Generated by Django 2.2.11 on 2020-06-07 16:13

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import pokryvala.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренд',
            },
        ),
        migrations.CreateModel(
            name='Pokryvala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит(Не трогать)')),
                ('key_words', models.CharField(blank=True, max_length=120, null=True, verbose_name='Ключи')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=pokryvala.models.image_folder, verbose_name='Фотка')),
                ('image_link', models.CharField(blank=True, max_length=120, null=True, verbose_name='Фотка ссылка')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена ')),
                ('price_old', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Старая цена ')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Текст')),
                ('description_short', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Текст(короткий)')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('is_active', models.BooleanField(default=True, verbose_name='В наличии')),
                ('new_product', models.BooleanField(default=False, verbose_name='Новинка')),
                ('top', models.BooleanField(default=False, verbose_name='В топе(на гл.странице)')),
                ('slider', models.BooleanField(default=False, verbose_name='Слайдер(на гл.странице)')),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('brend', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokryvala.Brend', to_field='name', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Подушки',
                'verbose_name_plural': 'Подушки',
            },
        ),
        migrations.CreateModel(
            name='Tkan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True, unique=True)),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит')),
            ],
            options={
                'verbose_name': 'Ткань',
                'verbose_name_plural': 'Ткань',
            },
        ),
        migrations.CreateModel(
            name='PokryvalaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=pokryvala.models.image_gallary_folder)),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит')),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokryvala.Pokryvala')),
            ],
        ),
        migrations.AddField(
            model_name='pokryvala',
            name='tkan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokryvala.Tkan', to_field='name', verbose_name='Ткань'),
        ),
    ]
