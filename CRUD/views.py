# crud/models.py (Exemplo)

from django.db import models
from .models import Pessoa 
from django.shortcuts import render, redirect
# PROVAVELMENTE NO SEU CRUD/views.py


# Importe seu modelo 'Pessoa' (ajuste o caminho se necessário)

# Certifique-se de que a função 'home' está no escopo de 'redirect'

# CRUD/views.py (Código Corrigido)

from django.shortcuts import render, redirect
# 🌟 OBRIGATÓRIO: APENAS IMPORTE O MODELO, NÃO O DEFINA AQUI!
from .models import Pessoa 

# Suas funções de View
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    vqtdpessoas = request.POST.get("qtd_pessoas")
    
    Pessoa.objects.create(
        nome=vnome,
        telefone=vtelefone,
        email=vemail,
        qtd_pessoas=vqtdpessoas
    )
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoa.delete()
    return redirect(home)
# CRUD/views.py




