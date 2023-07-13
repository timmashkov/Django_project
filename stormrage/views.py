from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add an article', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},]


def index(request):
    return HttpResponse(f'Still not working, sorry dude')


def welcome(request):
    """Функция представление для домашней страницы с html скриптом"""
    intel = Alpha.objects.all()
    cats = Fraction.objects.all()

    context = {
        'intel': intel,
        'cats': cats,
        'menu': menu,
        'title': 'The Alpha Tempest main page',
        'cat_selected': 0
    }

    return render(request, 'stormrage_templates/index.html', context=context)


def show_info(request):
    return render(request, 'stormrage_templates/info.html', {'menu': menu, 'title': 'All the intel you have to know'})


def PageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found cause, deal with it</h1>')


def about(request):
    return HttpResponse('The intel about this site')


add_page_options = ['Add a page', 'Show all the data']
def add_page(request):
    return render(request, 'stormrage_templates/add_page.html',
                  {'options': add_page_options, 'title': 'Add a page'})


def contact(request):
    return HttpResponse('Get a feedback')


def login(request):
    return redirect('add_page')


def read_data(request, post_id):
    return HttpResponse(f'Read about this id={post_id}')


def show_fraction(request, cat_id):
    intel = Alpha.objects.filter(cat_id=cat_id)
    cats = Fraction.objects.all()

    context = {
        'intel': intel,
        'cats': cats,
        'menu': menu,
        'title': 'Fraction site',
        'cat_selected': 0
    }

    return render(request, 'stormrage_templates/index.html', context=context)



