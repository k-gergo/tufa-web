from django.urls import path
from . import views # Importáljuk a nézeteket (views.py) ebből a mappából

# Egyedi név az URL konfigurációnak (jó gyakorlat)
#app_name = 'main_app'

urlpatterns = [
    # A gyökér URL (pl. http://127.0.0.1:8000/) a 'views.index' nézetet hívja.
    # A 'name='index'' segítségével később könnyen hivatkozhatunk erre az URL-re.
    path('', views.index, name='index'),

    
]