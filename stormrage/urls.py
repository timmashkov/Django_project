from django.urls import path
from .views import *


urlpatterns = [
    path('home/', index, name='home'),
    path('stormrage/<int:ind>/', showing),
    path('another/', alter_page),
]
