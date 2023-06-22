from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request):
    if request.GET:
        print(request.GET)
    else:
        print('No get request found')
    return HttpResponse(f'The webpage for stormrage api')


def showing(request, ind):
    return HttpResponse(f'<h1>Testing writings for the first time</h1><p>{ind}</p>')
# Create your views here.


def pageNotFound(request, exception):
    print(request.GET)
    return HttpResponseNotFound(f'<h1>Page not found cause {exception}</h1>')
