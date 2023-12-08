"""
Controla informações no 'admin' do Django.
------------------------------------------
admin.site.register(nome do Model) - Controla dentro do site de administração
os models que poderei inserir e remover registros;
Aqui pude controlar a quantidade das informações que eram exibidas 
através do nome de seus campos em list_display.

OBS: O arquivo admin.py serve para importar os modelos e registrar no 
aplicativo de administração.
"""
from django.contrib import admin
from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estoque', 'preco')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
