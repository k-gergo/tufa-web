# rampak/views.py
from django.shortcuts import render, get_object_or_404
from .models import RampakCategory, RampakProduct

def rampak_list(request):
    """Rámpák listázó oldala"""
    categories = RampakCategory.objects.all().prefetch_related('products')
    context = {
        'categories': categories,
        'page_title': 'Rámpák' # Oldalcím frissítve
    }
    return render(request, 'rampak/rampak_list.html', context)

def rampak_product_detail(request, product_id):
    """Rámpa részletező oldala"""
    product = get_object_or_404(RampakProduct, id=product_id)
    context = {
        'product': product,
        'page_title': product.name_hu
    }
    return render(request, 'rampak/rampak_product_detail.html', context)