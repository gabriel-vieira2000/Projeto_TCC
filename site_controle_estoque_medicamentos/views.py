from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'site/pages/home.html', context={
        'autor': 'Gabriel Vieira Cardoso',
        'titulo': 'Página Inicial - CEME',
        'testes': ['Teste 1', 'Teste 2'],
    })


def teste(request):
    return HttpResponse("Teste!")
