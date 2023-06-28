from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add an article', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}]


def index(request):
    return HttpResponse(f'Still not working, sorry dude')


def welcome(request):
    """Функция представление для домашней страницы с html скриптом"""
    intel = Alpha.objects.all()
    context = {
        'intel': intel,
        'menu': menu,
        'title': 'The Alpha Tempest main page'
    }
    return render(request, 'stormrage_templates/index.html', context=context)


def show_info(request):
    return render(request, 'stormrage_templates/info.html', {'menu': menu, 'title': 'All the intel you have to know'})


def PageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found cause, deal with it</h1>')


def about(request):
    return HttpResponse('The intel about this site')


def add_page(request):
    return HttpResponse('Add a page')


def contact(request):
    return HttpResponse('Get a feedback')


def login(request):
    return HttpResponse('Login your account')
