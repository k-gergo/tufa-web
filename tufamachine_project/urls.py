from django.contrib import admin
from django.urls import path, include # Fontos: 'include' importálása!
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tufadmin/', admin.site.urls),
    # Az összes többi URL kérést továbbítjuk a 'main_app.urls' fájlhoz
    path('kapcsolat/', include('contact.urls'), name='contact'),
    path('', include('main_app.urls')),
    path('erdeszeti-gepek/', include('forestry.urls', namespace='forestry')),
    path('epitoipari-gepek/', include('epiteszet.urls')),
    path('mezogazdasagi-gepek/', include('mezogazdasag.urls')),
    path('rampak/', include('rampak.urls')),
    path('hasznalt-gepek/', include('hasznalt.urls')),
    path('xcmg-gepek/', include('xcmg.urls')),
    path('galeria/', include('gallery.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)