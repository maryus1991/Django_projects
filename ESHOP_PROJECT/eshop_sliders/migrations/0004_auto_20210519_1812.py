# Generated by Django 3.1.5 on 2021-05-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_sliders', '0003_alter_slider_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]