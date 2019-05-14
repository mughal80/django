
from django.urls import path, include
from . import views

urlpatterns = [  
    path('', views.index, name="BlogHome"),
    path('about/', views.about, name="BlogAbout"),
]
