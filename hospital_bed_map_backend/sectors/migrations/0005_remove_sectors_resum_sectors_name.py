# Generated by Django 4.2 on 2023-06-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0004_alter_sectors_tip_acc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectors',
            name='resum',
        ),
        migrations.AddField(
            model_name='sectors',
            name='name',
            field=models.CharField(default='exit', max_length=15, unique=True, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
