from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


menu = ['About', 'Add an article', 'Feedback', 'Login']


def index(request):
    """функция представление домашней директории STORMRAGE с гет запросом"""
    if request.GET:
        print(request.GET)
    else:
        print('No get-request found')
    return HttpResponse(f'''<h1>The webpage for stormrage api</h1>''')


def showing(request, ind):
    """функция представление для STORMRAGE со слагом"""
    if ind <= 1000:
        return redirect('home', permanent=True)
    elif ind > 1000:
        raise Http404('too big number buddy')
    return HttpResponse(f'<h1>Testing writings for the first time</h1><p>{ind}</p>')
# Create your views here.


def alter_page(request):
    """Функция представление для вспомогательной страницы ANOTHER с гет запросом"""
    if request.GET:
        print(request.GET)
    else:
        print('Sorry, theres nothing')
    return HttpResponse(f'<h1>Alternative page, just testing django views, never mind</h1>')


def welcome(request):
    """Функция представление для домашней страницы с html скриптом"""
    intel = Alpha.objects.all()
    return render(request, 'stormrage_templates/index.html', {'intel': intel, 'menu': menu, 'title': 'The Alpha Tempest main page'})


def show_info(request):
    return render(request, 'stormrage_templates/info.html', {'menu': menu, 'title': 'All the intel you have to know'})


def PageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found cause, deal with it</h1>')