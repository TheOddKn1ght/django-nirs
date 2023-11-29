"""
URL configuration for nirs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views
from app.views import services, service_detail
from django.conf.urls import handler404
from app.views import custom_404
from app.views import doctors

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index' ),
    path('services', views.services, name='services'),
    path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('doctors', views.doctors, name='doctors'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail')
]
