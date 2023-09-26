from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request: index')
    return HttpResponse('<h2>Task 2(seminar3), working on a console, not web, check views.py view</h2>')
