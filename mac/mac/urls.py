from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('about', view.about, name ='About'),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls'))    
]
