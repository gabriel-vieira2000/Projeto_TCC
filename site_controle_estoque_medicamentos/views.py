from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'site/pages/home.html', context={
        'autor': 'Gabriel Vieira Cardoso',
        'titulo': 'Página Inicial - CEME'
    })


def teste(request):
    return HttpResponse("Teste!")
