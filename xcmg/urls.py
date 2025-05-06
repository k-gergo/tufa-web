# xcmg/urls.py
from django.urls import path
from . import views

app_name = 'xcmg' # Névtér

urlpatterns = [
    path('', views.xcmg_list, name='xcmg_list'), # Lista oldal neve
    path('gep/<int:product_id>/', views.xcmg_product_detail, name='product_detail'),
    # Vagy: path('termek/<int:product_id>/', ...)
]