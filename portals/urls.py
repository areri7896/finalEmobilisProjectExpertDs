"""
URL configuration for djangoFinalProject project.

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
from . import views as portals_views
from portals import views as portals_views

urlpatterns = [
    path('', portals_views.dashboard, name='dashboard'),
    path('login/', portals_views.login, name='login'),
    path('messages/', portals_views.messages, name='messages'),
    path('reciept/', portals_views.reciept, name='reciept'),
    path('payment/', portals_views.payment, name='payment'),
    path('statement/', portals_views.statement, name='statement'),
    path('maps/', portals_views.maps, name='maps'),
    path('settings/', portals_views.settings, name='settings'),
    path('profile/', portals_views.profile, name='profile'),
    path('academics/', portals_views.academics, name='academics'),
    path('admissions/', portals_views.admissions, name='admissions'),
    path('faqs/', portals_views.faqs, name='faqs'),
]
