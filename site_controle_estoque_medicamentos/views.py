from django.http import HttpResponse


# from django.shortcuts import render
# Create your views here.
def home(request):
    return HttpResponse("Página Inicial do Sistema")


def teste(request):
    return HttpResponse("Teste!")
