from django.shortcuts import render
from django.http  import HttpResponse


def index(request):
    """
    Renders the index page
    """
    return render(request, 'index.html')
