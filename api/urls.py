
from django.contrib import admin
from django.urls import path
from .views import api_views

urlpatterns = [
    path('', api_views),
]
