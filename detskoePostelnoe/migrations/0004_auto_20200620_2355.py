# Generated by Django 2.2.11 on 2020-06-20 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detskoePostelnoe', '0003_auto_20200613_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detskapostel',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='detskoePostelnoe.Type', to_field='name', verbose_name='Рисунок'),
        ),
    ]
