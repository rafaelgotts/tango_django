# -*- coding: utf-8 -*-
from django.http import HttpResponse


def index(request):
    """ Create an intro pago for Rango, like
        https://youtu.be/j7gp56w8T18?t=50s
    """
    response_body = (
        'My name is...Rango<p>'
        '<a href="/rango/about">Here</a> you can now more about me'
    )
    return HttpResponse(response_body)


def about(request):
    response_body = (
        'Rango Says: Here is the about page.</p>'
        '<a href="/rango/">Here</a> you can go back do index page.'
    )
    return HttpResponse(response_body)
