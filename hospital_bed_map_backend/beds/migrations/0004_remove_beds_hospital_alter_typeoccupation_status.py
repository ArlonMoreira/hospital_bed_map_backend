# Generated by Django 4.2 on 2023-07-24 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0003_alter_type_options_remove_typeoccupation_color_hex_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beds',
            name='hospital',
        ),
        migrations.AlterField(
            model_name='typeoccupation',
            name='status',
            field=models.CharField(choices=[('OCUPADO', 'OCUPADO'), ('RESERVADO', 'RESERVADO'), ('VAGO', 'VAGO'), ('BLOQUEADO', 'BLOQUEADO')], max_length=45, verbose_name='status'),
        ),
    ]
