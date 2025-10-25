"""
URL configuration for APP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# APP/urls.py

from django.contrib import admin
from django.urls import path, include # 👈 Garanta que 'include' está aqui!
from django.urls import path
from CRUD import views
urlpatterns = [
    # 1. URLs do Admin
    path('admin/', admin.site.urls),
   
    # 2. URLs do seu app CRUD
    # A rota vazia ('') significa que as URLs do CRUD serão carregadas na raiz do site.
    path('', include('CRUD.urls')), # 🚨 CORREÇÃO APLICADA AQUI 🚨
    



    path('', views.home, name='home'),
    path('reserva/', views.reserva, name='reserva'),



    path('admin/', admin.site.urls),
    path('', include('CRUD.urls')),  # Inclui as urls do app CRUD



   
    # Nota: Use o nome da pasta do seu app como string de importação: 'CRUD.urls'
]

