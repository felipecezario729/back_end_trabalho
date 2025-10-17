from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, delete
from . import views

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name = "salvar"),
    path('apagar/<int:id>', delete, name = "delete"),

    # Mapeia a URL raiz do app (ex: http://127.0.0.1:8000/) para a view 'home'
    path('', views.home, name='home'),
    
    # Mapeia a URL 'salvar/' para a view 'salvar'
    path('salvar/', views.salvar, name='url_para_salvar'),
    
    # Mapeia a URL 'delete/ID/' para a view 'delete'
    path('delete/<int:id>/', views.delete, name='url_para_deletar'),
    
    # Se precisar de um URL para edição:
    # path('update/<int:id>/', views.update, name='url_para_update'),
]