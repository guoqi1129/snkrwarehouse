from django import template
from snkrs.config import *
register = template.Library()

def get_keys(value):
    return list(value)[0]

def get_item_url(value):
    return ITEM_URLS[value]

register.filter("getkeys", get_keys)
register.filter("getitemurl", get_item_url)
