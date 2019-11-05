from django.db import models
from django.utils import timezone


"""armazento"""
GELADEIRA = 'GLD'
ARMARIO = 'ARM'
FREEZER = 'FRZ'
ARLIVRE = 'ALV'
armazenamentos = [
    (GELADEIRA, 'Geladeira'),
    (FREEZER, 'Freezer'),
    (ARMARIO, 'Armário'),
    (ARLIVRE, 'Ar livre'),
]

class Produto (models.Model):
    nome = models.CharField(max_length=100)
    data_compra = models.DateTimeField(default=timezone.now)
    data_validade = models.DateTimeField()
    quantidade = models.IntegerField(default=0)

    armazenamento = models.CharField(
        max_length= 4,
        choices = armazenamentos,
        default = 'ARLIVRE',
    )

    def comprar (self, quantidade):
       self.quantidade = self.quantidade + quantidade
       self.save()

    def utilizar (self, quantidade):
        self.quantidade = self.quantidade - quantidade
        self.save()

    def __str__(self):
        return self.nome
# Create your models here.
