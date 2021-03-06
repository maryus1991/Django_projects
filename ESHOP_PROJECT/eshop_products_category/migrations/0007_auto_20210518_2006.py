# Generated by Django 3.2.3 on 2021-05-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0006_delete_subproductcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='level',
            field=models.PositiveIntegerField(default=11, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='lft',
            field=models.PositiveIntegerField(default=11, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]
