from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('demo/', views.demo),
    path('canvas', views.canvas),
    path('image', views.image),
    path('clock', views.clock),
    path('card', views.card),
    path('loader', views.loader),
   
]