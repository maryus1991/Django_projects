# Generated by Django 3.2 on 2021-05-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
