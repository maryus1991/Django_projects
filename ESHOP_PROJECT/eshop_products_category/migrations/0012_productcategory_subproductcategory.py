# Generated by Django 3.2.3 on 2021-05-18 20:11

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0011_auto_20210518_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='SubProductCategory',
            field=mptt.fields.TreeForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_products_category.productcategory'),
        ),
    ]
