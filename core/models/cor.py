from django.db import models


class Cor(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return f'({self.id}) {self.nome}'

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'