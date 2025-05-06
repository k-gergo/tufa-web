# main_app/views.py

from django.shortcuts import render


def index(request):
    """Főoldal nézete dinamikus FeaturedProduct adatokkal"""

    
    context = {

        'page_title': 'Főoldal',
    }
    
    return render(request, 'index.html', context)
