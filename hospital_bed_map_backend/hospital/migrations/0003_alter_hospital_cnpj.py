# Generated by Django 4.2 on 2023-06-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_hospital_cnes_hospital_cnpj_alter_hospital_acronym_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True, verbose_name='cnpj'),
        ),
    ]
