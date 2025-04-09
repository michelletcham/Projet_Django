from django.urls import path
from .views import produits_list

urlpatterns = [
    path('produits/', produits_list, name='produits'),
]
