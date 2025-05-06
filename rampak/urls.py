# rampak/urls.py
from django.urls import path
from . import views

app_name = 'rampak' # Névtér az URL hivatkozásokhoz

urlpatterns = [
    path('', views.rampak_list, name='rampak_list'), # Lista oldal neve is frissítve
    path('reszletek/<int:product_id>/', views.rampak_product_detail, name='product_detail'),
    # Vagy használhatod a 'gep/' vagy 'termek/' útvonalat is itt, ha szeretnéd
]