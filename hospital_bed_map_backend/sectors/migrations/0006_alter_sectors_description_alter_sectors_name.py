# Generated by Django 4.2 on 2023-06-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0005_remove_sectors_resum_sectors_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectors',
            name='description',
            field=models.CharField(max_length=145, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Nome'),
        ),
    ]
