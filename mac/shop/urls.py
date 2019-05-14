
from django.urls import path, include
from . import views

urlpatterns = [  
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="ShopAbout"),
    path('contact/', views.contact, name="Shopcontact"),
    path('tracker/', views.tracker, name="ShopTracker"),
    path('search/', views.search, name="ShopSearch"),
    path('productview/', views.prodview, name="ShopProduct"),
    path('checkout/', views.checkout, name="ShopCheckout"),
   
]
