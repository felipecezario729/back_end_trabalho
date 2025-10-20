from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'qtd_pessoas', 'hora_chegada', 'atendido')
    search_fields = ('nome', 'email', 'telefone')
    list_filter = ('atendido', 'hora_chegada')
    list_editable = ('atendido',)  # para poder marcar como atendido diretamente na lista

admin.site.register(Pessoa, PessoaAdmin)
