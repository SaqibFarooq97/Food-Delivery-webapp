# Generated by Django 3.1.4 on 2020-12-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0010_auto_20201225_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='processed_by',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
