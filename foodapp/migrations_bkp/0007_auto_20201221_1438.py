# Generated by Django 3.1.4 on 2020-12-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_auto_20201220_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(max_length=300, verbose_name='password'),
        ),
    ]
