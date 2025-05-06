# forestry/urls.py
from django.urls import path
from . import views

app_name = 'forestry' # Névtér az URL-eknek

urlpatterns = [
    path('', views.forestry_list, name='forestry_list'), # Az app gyökere a listaoldal
    path('product/<int:product_id>/', views.forestry_product_detail, name='product_detail'),
    path('forestry-product/<int:product_id>/', views.forestry_product_detail, name='forestry_product_detail'),
]