# Generated by Django 3.1.5 on 2021-05-19 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0016_auto_20210519_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
