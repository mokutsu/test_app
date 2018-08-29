"""testproj URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('testapp.urls')),
    path('', include('frontend.urls')),

]
