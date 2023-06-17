from django.db import models
from django.conf import settings
from ..hospital.models import Hospital

# Create your models here.
class TypeAccommodation(models.Model):
    description = models.CharField('Descrição', blank=False, null=False, max_length=45)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Tipo de acomodação'
        verbose_name_plural = 'Tipos de acomodação'

class Sectors(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        verbose_name='Hospital',
        blank=False,
        null=False
    )
    name = models.CharField('Nome', blank=False, null=False, max_length=15)
    description = models.CharField('Descrição', blank=False, null=False, max_length=145)
    tip_acc = models.ForeignKey(
        TypeAccommodation,
        on_delete=models.SET_NULL,
        verbose_name='Tipo Acomodação',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='ativo',
        default=True
    )
    activation_date = models.DateTimeField(
        'Data de ativação',
        blank=True,
        null=True
    )
    deactivation_date = models.DateTimeField(
        'Data de desativação',
        blank=True,
        null=True
    )
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
        return self.resum
    
    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'