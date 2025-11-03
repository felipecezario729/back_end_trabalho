from django.shortcuts import render, redirect,get_object_or_404
from .models import Pessoa



# Create your views here.

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoas})

def salvar(request):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    Pessoa.objects.create(nome=vnome,idade=vidade)
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{"pessoas":pessoas})

def delete(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoa.delete()
    return redirect(home)

def editar(request, id):
    pessoas = Pessoa.objects.get(id = id)
    return render(request,"update.html",{"pessoa":Pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    pessoa = Pessoa.objects.get(id = id)
    pessoa.nome = vnome
    pessoa.idade = vidade
    pessoa.save()
    return redirect(home)







