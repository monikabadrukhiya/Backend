"""
URL configuration for hospitalwebproject project.

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
    path('about',views.About),
    path('appoinment',views.Appoinment),
    path('blogsidebar',views.Blogsidebar),
    path('blogsingle',views.Blogsingle),
    path('confirmation',views.Confirmation),
    path('contact',views.Contact),
    path('departmentsingle',views.Departmentsingle),
    path('department',views.Department),
    path('doctorsingle',views.Doctorsingle),
    path('doctor',views.Doctor),
    path('documentation',views.Documentation),
    path('service',views.Service),
    path('admin/', admin.site.urls),
]
