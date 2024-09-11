"""
URL configuration for untreewebproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home,name='Home'),
    path('add',views.Add,name='add'),
    path('contactdata',views.Contactdata),
    path('about',views.About,name='About'),
    path('blog',views.Blog,name='Blog'),
    path('cart',views.Cartt,name='Cart'),
    path('data',views.Cartdata,name='Cartldata'),
    path('delete',views.Delete),
    path('quantity',views.Quantitty),
    path('checkout',views.Checkout,name='Checkout'),
    path('contact',views.Contact,name='Contact'),
    path('services',views.Service,name='Service'),
    path('shop',views.Shop,name='Shop'),
    path('thankyou',views.Thankyou,name='Thankyou'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
   if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
