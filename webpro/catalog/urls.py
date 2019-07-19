"""webpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dnac/', views.dnac, name='dnac'),
    path('dnac/api1/', views.dnac_api1, name='dnac_api1'),
    path('dnac/api2/', views.dnac_api2, name='dnac_api2'),
    path('meraki/', views.meraki, name='meraki'),
    path('iosxe/', views.iosxe, name='iosxe'),
    path('sdwan/', views.sdwan, name='sdwan'),
]
