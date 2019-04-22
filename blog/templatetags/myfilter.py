# coding=utf-8

from django.template import Library
import datetime
register = Library()

@register.filter
def def_format(value, pattern):
    value = value.strftime(pattern)
    return value

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)

@register.filter
def Y_m(value):
    a = value.split('-')
    return '{}年{}月'.format(a[0],a[1])