"""
URL configuration for qrapp project.

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
from home import views



urlpatterns = [
    path('', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('home/', views.home.as_view(), name='home'),
    path('about/', views.about.as_view(), name='about'),
    path('contact/', views.contact.as_view(), name='contact'),
    path('services/', views.services.as_view(), name='services'),
    path('form/', views.signup, name='signup'),
    path('privacypolicy/', views.privacypolicy.as_view(), name='privacypolicy'),
    #path('login/', views.index, name = 'index'),  
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate, name='activate'),  
]
