# Generated by Django 3.2.3 on 2021-06-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sliders', '0004_auto_20210519_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
