"""
URL configuration for environmentweb project.

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

urlpatterns = [
    path('',views.Home),
    path('error',views.Erroe404),
    path('about',views.About),
    path('blog',views.Blog),
    path('causes',views.Causes),
    path('contact',views.Contact),
    path('donation',views.Donation),
    path('event',views.Event),
    path('gallary',views.Gallary),
    path('service',views.Service),
    path('volunteer',views.Volunteer),
    path('admin/', admin.site.urls),
]
