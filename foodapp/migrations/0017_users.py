# Generated by Django 3.1.4 on 2021-01-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0016_food_items_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=300, null=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=300, verbose_name='password')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='address')),
            ],
        ),
    ]