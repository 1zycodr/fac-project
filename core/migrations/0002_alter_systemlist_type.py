# Generated by Django 4.0.5 on 2022-06-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemlist',
            name='type',
            field=models.IntegerField(choices=[(0, 'PROCEDURE'), (1, 'OBJECT'), (2, 'PACKAGE')], verbose_name='Тип'),
        ),
    ]
