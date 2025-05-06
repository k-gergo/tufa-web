# epiteszet/urls.py
from django.urls import path
from . import views  # Importáljuk a nézeteket az aktuális (epiteszet) mappából

# app_name: Ez egy névtér (namespace). Segít elkerülni az URL név ütközéseket
# más appokkal a projektben. Így hivatkozol rá a templatekben: {% url 'epiteszet:url_neve' %}
app_name = 'epiteszet'

urlpatterns = [
    # Az app gyökér URL-je (pl. /epiteszeti-gepek/)
    # Ezt a '' mintázat fogja elkapni, és az epiteszet_list nézetet hívja meg.
    # A 'name' argumentummal adunk neki egy nevet, amivel hivatkozhatunk rá.
    path('', views.epiteszet_list, name='epiteszet_list'),

    # A termék részletező oldal URL-je (pl. /epiteszeti-gepek/gep/123/)
    # A 'gep/<int:product_id>/' mintázat egy 'gep/' szót vár, amit egy egész szám követ.
    # Az <int:product_id> rész "elfogja" a számot, és átadja a nézetnek 'product_id' néven.
    # Az epiteszet_product_detail nézetet hívja meg.
    path('reszletek/<int:product_id>/', views.epiteszet_product_detail, name='product_detail'),

    # Ide jöhetnek további URL minták az epiteszet apphoz, ha szükséges.
]