from django import template
from stormrage.models import *

register = template.Library()

@register.simple_tag()
def get_fractions():
    return Fraction.objects.all()
