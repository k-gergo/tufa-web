# xcmg/views.py
from django.shortcuts import render, get_object_or_404
from .models import XcmgCategory, XcmgProduct

def xcmg_list(request):
    """XCMG gépek listázó oldala"""
    categories = XcmgCategory.objects.all().prefetch_related('products')
    context = {
        'categories': categories,
        'page_title': 'XCMG Gépek' # Oldalcím frissítve
    }
    return render(request, 'xcmg/xcmg_list.html', context)

def xcmg_product_detail(request, product_id):
    """XCMG gép részletező oldala"""
    product = get_object_or_404(XcmgProduct, id=product_id)
    context = {
        'product': product,
        'page_title': product.name_hu
    }
    return render(request, 'xcmg/xcmg_product_detail.html', context)