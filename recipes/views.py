
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return http request
    return render(request, 'recipes/home.html', status=200, context={'name': 'Juliano', })


def sobre(request):
    # return http request
    return render(request, 'temp/temp.html')


def contato(request):
    # return http request
    return HttpResponse('Contato')
