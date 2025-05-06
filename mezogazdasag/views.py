# mezogazdasag/views.py
from django.shortcuts import render, get_object_or_404
from .models import MezogazdasagCategory, MezogazdasagProduct

def mezogazdasag_list(request):
    """Mezőgazdasági gépek listázó oldala"""
    categories = MezogazdasagCategory.objects.all().prefetch_related('products')
    context = {
        'categories': categories,
        'page_title': 'Mezőgazdasági gépek' # Oldalcím frissítve
    }
    # Új sablon használata
    return render(request, 'mezogazdasag/mezogazdasag_list.html', context)

def mezogazdasag_product_detail(request, product_id):
    """Mezőgazdasági gép részletező oldala"""
    product = get_object_or_404(MezogazdasagProduct, id=product_id)
    context = {
        'product': product,
        'page_title': product.name_hu
    }
    # Új, app-specifikus sablon használata
    return render(request, 'mezogazdasag/mezogazdasag_product_detail.html', context)