from django import template
from stormrage.models import *

register = template.Library()

@register.simple_tag()
def get_fractions():
    return Fraction.objects.all()

@register.inclusion_tag('stormrage/list_fractions.html')
def show_data():
    cats = Fraction.objects.all()
    return {'cats': cats}
