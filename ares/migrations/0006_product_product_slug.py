# Generated by Django 4.0.1 on 2022-01-23 08:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ares', '0005_alter_product_image_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_slug',
            field=autoslug.fields.AutoSlugField(default='1', editable=False, populate_from='product_name'),
        ),
    ]
