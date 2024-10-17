"""
URL configuration for studentadminpanel project.

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
from.import views

urlpatterns = [
    path('',views.Login),
    path('home',views.Home),
    path('todaycall',views.Todaycall),
    path('countinquirydata',views.Countinquiry),
    path('addformdata',views.addform),
    path('viewdata',views.Viewform),
    path('addmission',views.Addmissionform),
    path('ragister',views.Register),
    path('logindata',views.Logindata),
    path('delete',views.Deletedata),
    path('admissiondata',views.admissiondata),
    path('totaladmission',views.totaladmission),
    path('inquirydata',views.Inquirydata),
    path('edit',views.Editdata),
    # path('searchdata',views.Searchdata),
    path('admin/', admin.site.urls),
]
