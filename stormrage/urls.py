from django.urls import path
from .views import *


urlpatterns = [
    path('', welcome, name='home'),
    path('info/', show_info, name='info'),
    path('stormrage/', index),
    path('about', about, name='about'),
    path('add_page', add_page, name='add_page'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
]
