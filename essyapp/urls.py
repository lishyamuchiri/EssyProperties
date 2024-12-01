
from django.contrib import admin
from django.urls import path

from essyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book, name='book'),

]
