# Generated by Django 3.1.2 on 2020-11-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0055_auto_20201031_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='karma',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Карма'),
        ),
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.TextField(help_text='Краткое описание назначения приложения.', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='app',
            name='text_src',
            field=models.TextField(help_text='Более подробное описание назначения и функциональных особенностей приложения.', verbose_name='Исходный текст'),
        ),
    ]