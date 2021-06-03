# Here we can create our own/custom template filters

from django import template

register = template.Library()

# @register.filter(name='cut')
def cut(value,arg):                # Value is the the value returned by context dictionary in views.py filter
    """
    This cuts out all values of 'arg' from the values
    """

    return value.replace(arg,'')

register.filter('nikhil',cut)       # Nikhil is the value that we use in template tagging in HTML file and cut refers to the function we defined above
