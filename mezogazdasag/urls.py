# mezogazdasag/urls.py
from django.urls import path
from . import views

app_name = 'mezogazdasag' # Névtér az URL hivatkozásokhoz

urlpatterns = [
    path('', views.mezogazdasag_list, name='mezogazdasag_list'), # Lista oldal neve is frissítve
    # Használhatjuk ugyanazt az URL struktúrát és nevet a részletezőhöz
    path('termek/<int:product_id>/', views.mezogazdasag_product_detail, name='product_detail'),
    # Vagy ha szeretnéd: path('termek/<int:product_id>/', ...)
]