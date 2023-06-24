from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    if request.GET:
        print(request.GET)
    else:
        print('No get-request found')
    return HttpResponse(f'The webpage for stormrage api')


def showing(request, ind):
    if ind >= 10:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Testing writings for the first time</h1><p>{ind}</p>')
# Create your views here.


def alter_page(request):
    if request.GET:
        print(request.GET)
    else:
        print('Sorry, theres nothing')
    return HttpResponse(f'<h1>Alternative page, just testing django views, never mind</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found cause, deal with it</h1>')
