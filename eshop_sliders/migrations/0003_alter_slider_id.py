# Generated by Django 3.2 on 2021-05-10 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sliders', '0002_auto_20210510_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
