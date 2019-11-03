from django import template
from snkrs.config import *
register = template.Library()

def get_keys(value):
    return list(value)[0]

def get_value(value):
    return list(value.values())[0]

def get_num(value):
    return len(value)

register.filter("getkeys", get_keys)
register.filter("getvalue", get_value)
register.filter("getnum", get_num)
