# Generated by Django 2.2.11 on 2020-06-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podushki', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podushki',
            name='filler_weight',
        ),
        migrations.DeleteModel(
            name='FillerWeight',
        ),
    ]
