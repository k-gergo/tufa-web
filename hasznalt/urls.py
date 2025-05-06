# hasznalt/urls.py
from django.urls import path
from . import views

app_name = 'hasznalt' # Névtér

urlpatterns = [
    path('', views.hasznalt_list, name='hasznalt_list'), # Lista oldal neve
    path('reszletek/<int:product_id>/', views.hasznalt_product_detail, name='product_detail'),
    # Vagy: path('reszletek/<int:product_id>/', ...)
]