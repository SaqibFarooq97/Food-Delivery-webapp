# Generated by Django 3.1.4 on 2021-03-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0034_file_item_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='file',
            new_name='file_upload',
        ),
    ]
