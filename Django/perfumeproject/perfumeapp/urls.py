"""
URL configuration for perfumeproject project.

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
    path('',views.Home,name="index"),
    path('header',views.categories_processor,name="header"),
    path('logindataapp',views.Login_data,name="logindataapp"),
    path('ragisterapp',views.Ragister_data,name="ragisterapp"),
    path('logout',views.Logout,name="logout"),
    path('category',views.categorywisedata,name="category"),
    path('shop',views.shopdata,name="shop"),
    path('about',views.About,name="about"),
    path('contact',views.Contactdata,name="contact"),
    path('quantity',views.Quantity,name="quantity"),
    path('cart',views.Cart,name="cart"),
    path('cartdata',views.Cart_data,name="cartdata"),
    path('delete',views.Delete_cartdata,name="delete"),
    path('discription',views.Discription,name="discription"),
    path('checkoutdata',views.cheoutdata,name="checkoutdata"),
    path('checkout',views.Checkout,name="checkout"),
    path('thankyou',views.Thankyou,name="thankyou"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 