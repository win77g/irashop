# Generated by Django 2.2.11 on 2020-04-08 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_advertisingimagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisingimagemodel',
            name='slug',
        ),
    ]
