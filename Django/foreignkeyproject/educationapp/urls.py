"""
URL configuration for foreignkeyproject project.

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
from .import views

urlpatterns = [
    path('',views.Eduget),
    path('create/',views.Educreate),
    path(' <int:efilterid>/',views.Edufilter),
    path('delete/<int:edeleteid>/',views.Edudelete),
    path('update/<int:eupdateid>/',views.Eduupdate),

    # path('femget/',views.Familyget),
    # path('femcreate/',views.Familycreate),
    # path('femfilter/<int:ffilterid>/',views.Familyfilter),
    # path('femdelete/<int:fdeleteid>/',views.Familydelete),
    # path('femupdate/<int:fupdateid>/',views.Familyupdate),

    path('admin/', admin.site.urls),
]
