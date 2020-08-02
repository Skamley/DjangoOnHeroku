from django import template

register= template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This is a custom filter used. This cuts out all values of arg from the string
    :param value: The entire string will be passed from template
    :param arg: The specific word we need to exclude of the string
    :return: value - arg
    """
    finalString = value.replace(arg,"")
    return finalString

