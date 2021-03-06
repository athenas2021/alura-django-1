from django.db import models
# from datetime import datetime
from django.utils import timezone

class Receita(models.Model):
    nome_receita = models.CharField(max_length=150)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateField(default=timezone.now, blank=True)