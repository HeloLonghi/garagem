from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos')
    acessorios = models.ManyToManyField(Acessorio, blank=True, related_name='veiculos')

    def __str__(self):
        return f'({self.id}) {self.modelo.nome} - {self.cor.nome} {self.ano or ""}'

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
