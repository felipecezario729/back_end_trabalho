from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    qtd_pessoas = models.IntegerField()
    hora_chegada = models.DateTimeField(default=timezone.now)  # <- corrigido aqui
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} {self.telefone} {self.email} {self.qtd_pessoas} {self.hora_chegada} {self.atendido}"

