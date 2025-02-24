# Generated by Django 3.2.16 on 2024-12-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date'], 'verbose_name': 'публикация', 'verbose_name_plural': 'публикации'},
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(help_text='Если установить дату и время в будущем— можно делать отложенные публикации.', verbose_name='Дата и время публикации'),
        ),
    ]
