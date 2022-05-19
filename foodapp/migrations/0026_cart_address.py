# Generated by Django 3.1.4 on 2021-03-02 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0025_auto_20210302_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='address'),
            preserve_default=False,
        ),
    ]
