# hasznalt/views.py
from django.shortcuts import render, get_object_or_404
from .models import HasznaltCategory, HasznaltProduct

def hasznalt_list(request):
    """Használt gépek listázó oldala"""
    categories = HasznaltCategory.objects.all().prefetch_related('products')
    context = {
        'categories': categories,
        'page_title': 'Használt Gépek' # Oldalcím frissítve
    }
    return render(request, 'hasznalt/hasznalt_list.html', context)

def hasznalt_product_detail(request, product_id):
    """Használt gép részletező oldala"""
    product = get_object_or_404(HasznaltProduct, id=product_id)
    context = {
        'product': product,
        'page_title': product.name_hu
    }
    # Itt is hozzáadhatnál az új mezőkből a contexthez, ha a template-ben meg akarod jeleníteni
    return render(request, 'hasznalt/hasznalt_product_detail.html', context)