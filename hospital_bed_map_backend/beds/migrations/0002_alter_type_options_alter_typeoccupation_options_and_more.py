# Generated by Django 4.2 on 2023-07-23 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Tipo de ocupação', 'verbose_name_plural': 'Tipo de ocupações'},
        ),
        migrations.AlterModelOptions(
            name='typeoccupation',
            options={'verbose_name': 'Tipo de ocupação', 'verbose_name_plural': 'Tipo de ocupações'},
        ),
        migrations.RemoveField(
            model_name='typeoccupation',
            name='code',
        ),
        migrations.AddField(
            model_name='typeoccupation',
            name='status',
            field=models.CharField(choices=[('VAGO', 'VAGO'), ('BLOQUEADO', 'BLOQUEADO'), ('OCUPADO', 'OCUPADO'), ('RESERVADO', 'RESERVADO')], default=1, max_length=45, verbose_name='status'),
            preserve_default=False,
        ),
    ]
