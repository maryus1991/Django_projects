# Generated by Django 3.2.3 on 2021-06-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.CharField(default=1, max_length=150, verbose_name='ایمیل'),
            preserve_default=False,
        ),
    ]
