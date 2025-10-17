from django.db import models

# Create your models here.
# CRUD/models.py (Deve conter apenas a definição do modelo)

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    qtd_pessoas = models.IntegerField()
    # ... outros métodos ou metadados, se houver ...
    
 
    def __str__(self):
        return f"{self.nome} {self.telefone} {self.email} {self.qtd_pessoas}"
