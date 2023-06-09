from django.db import models
from django.conf import settings

# Hospitais
class Hospital(models.Model):
    cnes = models.CharField(
        verbose_name='cnes',
        max_length=7,
        unique=True,
        blank=False,
        null=False
    )
    cnpj = models.CharField(
        verbose_name='cnpj',
        max_length=18,
        unique=True,
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name='nome',
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )
    acronym = models.CharField(
        verbose_name='sigla',
        max_length=10,
        unique=True,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        verbose_name='ativo',
        default=True
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
        return self.name

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitais'