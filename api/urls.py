
from django.contrib import admin
from django.urls import path
from .views import api_views,api_post

urlpatterns = [
    path('', api_views),
    path('post/',api_post)
]
