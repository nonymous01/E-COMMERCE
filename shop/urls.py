from django.contrib import admin
from django.urls import path
from .views import shop,commande,panier
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', shop, name='shop'),
    path('commande/', commande, name='commande'),
    path('panier/', panier, name='commandepanier'),
    

]
