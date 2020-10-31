from django import template

register = template.Library()


@register.filter()
#Funcion de filtro
def price_format(value):
    return '${0:.2f}'.format(value)