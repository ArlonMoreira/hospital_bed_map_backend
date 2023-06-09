# Generated by Django 4.2 on 2023-06-16 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0006_alter_hospital_acronym'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAccommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=45, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resum', models.CharField(max_length=15, verbose_name='Resumo')),
                ('description', models.CharField(max_length=145, verbose_name='Descrição')),
                ('is_active', models.BooleanField(default=True, verbose_name='ativo')),
                ('activation_date', models.DateTimeField(verbose_name='Data de ativação')),
                ('deactivation_date', models.DateTimeField(verbose_name='Data de desativação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital', verbose_name='Hospital')),
                ('tip_acc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sectors.typeaccommodation', verbose_name='Tipo Acomodação')),
            ],
        ),
    ]
