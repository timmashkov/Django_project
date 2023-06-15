from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('The webpage for stormrage api')


def showing(request, ind):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Testing writings for the first time</h1><p>{ind}</p>')
# Create your views here.


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found cause {exception}</h1>')
