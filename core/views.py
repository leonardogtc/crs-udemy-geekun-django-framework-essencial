"""
Por esse arquivo posso: 
1. Listar a relação de produtos no banco de dados ou qualquer outra informação.
2. Passando informações para a página
"""
from django.shortcuts import render
from .models import Produto


def index(request):
    prods = Produto.objects.all()
    context = {
        'curso': 'Curso de Django da Geek University',
        'aluno': 'Leonardo G.T. da Conceição',
        'produtos': prods,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def handler500(request):
    return render(request, '404.html')

def handler404(request, exception):
    return render(request, '404.html')
