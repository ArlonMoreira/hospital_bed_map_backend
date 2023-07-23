from django.db import models
from hospital_bed_map_backend.hospital.models import Hospital
from hospital_bed_map_backend.sectors.models import Sectors
from django.conf import settings

class Type(models.Model):
    description = models.CharField('Descrição', blank=False, null=False, max_length=45)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de ocupação'
        verbose_name_plural = 'Tipo de ocupações'

class TypeOccupation(models.Model):
    code = models.CharField('Code', blank=False, null=False, max_length=1)
    description = models.CharField('Descrição', blank=False, null=False, max_length=45)
    color_hex = models.CharField('color', blank=False, null=False, max_length=7)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de ocupação'
        verbose_name_plural = 'Tipo de ocupações'

# Create your models here.
class Beds(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        verbose_name='Hospital',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    sector = models.ForeignKey(
        Sectors,
        verbose_name='Setor',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    name = models.CharField('Nome', blank=False, null=False, max_length=45)
    type_occupation = models.ForeignKey(
        TypeOccupation,
        verbose_name='Tipo de ocupação',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    type_occupation_description = models.TextField('Descrição tipo de ocupação', blank=False, null=False, max_length=255)
    type = models.ForeignKey(
        Type,
        verbose_name='Tipo',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    is_active = models.BooleanField('Ativo', default=True)
    is_extra = models.BooleanField('Extra', default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='usuario',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'



