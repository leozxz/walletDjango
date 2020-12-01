from django.db import models

class Moeda(models.Model):
    nome_moeda = models.CharField(max_length=15)
    valor_moeda = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nome_moeda

class Transacao(models.Model):
    real = models.DecimalField(max_digits=9, decimal_places=2)
    cripto = models.DecimalField(max_digits=9, decimal_places=2)

