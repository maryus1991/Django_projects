# Generated by Django 3.2 on 2021-05-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0002_alter_productcategory_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('name', models.CharField(max_length=150, verbose_name=' عنوان در URL ')),
                ('active', models.BooleanField(blank=True, default=True, verbose_name='فعال / غیر فعال')),
                ('category', models.ManyToManyField(to='eshop_products_category.ProductCategory')),
            ],
        ),
    ]
