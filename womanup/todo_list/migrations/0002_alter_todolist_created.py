# Generated by Django 4.1.3 on 2022-11-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
