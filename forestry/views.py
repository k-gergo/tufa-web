# forestry/views.py
from django.shortcuts import render, get_object_or_404
from .models import ForestryCategory, ForestryProduct

def forestry_list(request):
    """Erdészeti gépek listázó oldala"""
    categories = ForestryCategory.objects.all().prefetch_related('products')
    context = {
        'categories': categories,
        'page_title': 'Erdészeti gépek' # Oldalcím átadása
    }
    # Egy új sablont fogunk használni
    return render(request, 'forestry/forestry_list.html', context)

def forestry_product_detail(request, product_id):
    """Erdészeti gép részletező oldala"""
    product = get_object_or_404(ForestryProduct, id=product_id)
    context = {
        'product': product,
        'page_title': product.name_hu # Oldalcím a termék neve
    }
    # Egy új sablont fogunk használni
    return render(request, 'forestry/forestry_product_detail.html', context)