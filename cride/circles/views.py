""" Circles Views """

#Django
from django.http import HttpResponse



def list_circles(request):
    """List Circles. """
    return HttpResponse('Hola')