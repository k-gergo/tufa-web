# contact/views.py
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _ # Fordításhoz

def contact_page(request):
    """Megjeleníti a statikus kapcsolat és pályázatok oldalt."""
    context = {
        'page_title': _("Kapcsolat és Pályázatok")
    }
    # A sablont a templates/contact/contact_page.html helyen fogja keresni
    return render(request, 'contact/contact_page.html', context)

def warranty_view(request):
    context = {
        'page_title': _("Garanciális megállapodás")
    }
    return render(request, 'contact/warranty.html', context)