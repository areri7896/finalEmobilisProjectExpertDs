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
from . import views as expert_views
from portals import views as portals_views

urlpatterns = [
    path('', expert_views.home, name='home'),
    path('team/', expert_views.team, name='team'),
    path('about/', expert_views.about, name='about'),
    path('courses/', expert_views.courses, name='courses'),
    path('feature/', expert_views.feature, name='feature'),
    path('testimonial/', expert_views.testimonial, name='testimonial'),
    path('appointment/', expert_views.appointment, name='appointment'),
    path('404/', expert_views.error, name='error'),
    path('contact/', expert_views.contact, name='contact'),
    path('terms/', expert_views.terms, name='terms-and-conditions'),
    # path('portal/', portals_views.dashboard, name='portal'),
    # path('profile/', portals_views.profile, name='profile'),
]
