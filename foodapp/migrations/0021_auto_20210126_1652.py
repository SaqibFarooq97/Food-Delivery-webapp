# Generated by Django 3.1.4 on 2021-01-26 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0020_auto_20210126_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsignup',
            name='items',
        ),
        migrations.AddField(
            model_name='food_items',
            name='restaurent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foodapp.newsignup'),
            preserve_default=False,
        ),
    ]
