# Generated by Django 3.1.4 on 2021-03-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0026_cart_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='added_to_cart',
            field=models.BooleanField(default=False),
        ),
    ]