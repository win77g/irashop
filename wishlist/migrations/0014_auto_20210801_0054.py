# Generated by Django 2.2.11 on 2021-07-31 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0013_wishlistdpmodel_image_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlistdpmodel',
            options={'verbose_name': 'Товар в желаниях', 'verbose_name_plural': 'Товары в желаниях'},
        ),
        migrations.AlterModelOptions(
            name='wishlistmodel',
            options={'verbose_name': 'Товар в желаниях', 'verbose_name_plural': 'Товары в желаниях'},
        ),
    ]
