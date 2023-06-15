from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('The webpage for stormrage api')


def showing(request):
    return HttpResponse('<h1>Testing writings for the frist time</h1>')
# Create your views here.
