from django import template

register = template.Library()

@register.filter(name='getkey')
def getkey(value, arg):
    ''' Gets a value from a dict by key.  This allows keys to contain spaces, dashes, etc. '''
    return value.get(arg, '')
