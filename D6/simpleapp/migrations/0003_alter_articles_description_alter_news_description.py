# Generated by Django 4.1.5 on 2023-02-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(default='Ваша статья'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default='Ваша новость'),
        ),
    ]
