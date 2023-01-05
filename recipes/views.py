
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return http request
    return HttpResponse('Hello World')


def sobre(request):
    # return http request
    return HttpResponse('Sobre')


def contato(request):
    # return http request
    return HttpResponse('Contato')
