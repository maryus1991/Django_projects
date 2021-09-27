# Generated by Django 3.2.3 on 2021-05-18 20:16

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0013_auto_20210518_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='SubProductCategory',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cildren', to='eshop_products_category.productcategory'),
        ),
    ]