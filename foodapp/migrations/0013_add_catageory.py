# Generated by Django 3.1.4 on 2021-01-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0012_auto_20210123_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_catageory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_catagory', models.CharField(max_length=40, verbose_name='add_catageory')),
            ],
        ),
    ]