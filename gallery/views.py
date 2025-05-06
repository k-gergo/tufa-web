# gallery/views.py
from django.shortcuts import render
from .models import GalleryImage

def gallery_view(request):
    """Megjeleníti a galéria oldalt az összes képpel."""
    images = GalleryImage.objects.all() # Lekérdezzük az összes képet (a modell orderingje szerint)
    context = {
        'images': images,
        'page_title': "Galéria" # Oldalcím
    }
    return render(request, 'gallery/gallery_page.html', context)