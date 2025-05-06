# gallery/urls.py
from django.urls import path
from . import views

app_name = 'gallery' # Névtér az URL hivatkozásokhoz

urlpatterns = [
    # A galéria app gyökér URL-je (pl. /galeria/) a gallery_view nézetet hívja.
    path('', views.gallery_view, name='gallery_list'),
]