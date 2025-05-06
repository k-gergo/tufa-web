# epiteszet/views.py
from django.shortcuts import render, get_object_or_404
from .models import EpiteszetCategory, EpiteszetProduct

def epiteszet_list(request):
    """Építészeti gépek listázó oldala"""
    categories = EpiteszetCategory.objects.all().prefetch_related('products')
    context = {
        'categories': categories,
        'page_title': 'Építészeti gépek' # Oldalcím átadása
    }
    # Új sablon használata
    return render(request, 'epiteszet/epiteszet_list.html', context)

def epiteszet_product_detail(request, product_id):
    """Építészeti gép részletező oldala"""
    product = get_object_or_404(EpiteszetProduct, id=product_id)
    context = {
        'product': product,
        'page_title': product.name_hu # Oldalcím a termék neve
    }
    # Új, app-specifikus sablon használata
    return render(request, 'epiteszet/epiteszet_product_detail.html', context)