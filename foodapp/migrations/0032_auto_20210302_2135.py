# Generated by Django 3.1.4 on 2021-03-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0031_auto_20210302_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_items',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='newsignup',
            name='restaurentimage',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
