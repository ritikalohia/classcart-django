# Generated by Django 4.0.1 on 2022-01-22 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ares', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imagedata',
            new_name='image_data',
        ),
    ]