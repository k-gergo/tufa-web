# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost, Category # BlogImage itt nem szükséges

def blog_list(request):
    """Blog bejegyzések listázása, lapozással."""
    all_posts = BlogPost.objects.filter(status='published').select_related('category').order_by('-published')

    paginator = Paginator(all_posts, 9)  # 9 bejegyzés oldalanként
    page_number = request.GET.get('page')

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Ha a 'page' paraméter nem szám, az első oldalt mutatjuk
        posts = paginator.page(1)
    except EmptyPage:
        # Ha a 'page' paraméter túl nagy, az utolsó oldalt mutatjuk
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all() # Ha szükség van rá a sablonban (pl. oldalsáv)

    context = {
        'posts': posts, # Az aktuális oldal bejegyzései
        'categories': categories, # Minden kategória
        'is_paginated': posts.has_other_pages(), # Csak akkor jelenítjük meg a lapozót, ha több oldal van
    }

    return render(request, 'blog/blog_list.html', context)

def post_detail(request, slug):
    # Az optimalizálást a QuerySet-re alkalmazzuk, MIELŐTT lekérdezzük az objektumot
    queryset = BlogPost.objects.select_related('category').prefetch_related('gallery_images')
    post = get_object_or_404(queryset, slug=slug, status='published')

    # Legutóbbi 3 másik bejegyzés (kivéve az aktuálisat)
    recent_posts = BlogPost.objects.filter(status='published') \
                                     .exclude(id=post.id) \
                                     .select_related('category') \
                                     .order_by('-published')[:3]

    context = {
        'post': post,
        'recent_posts': recent_posts,
    }

    return render(request, 'blog/post_detail.html', context)

