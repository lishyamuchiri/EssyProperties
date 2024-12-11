
from django.contrib import admin
from django.urls import path

from essyapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book, name='book'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('cshow/', views.cshow, name='cshow'),
    path('bookshow/', views.bookshow, name='bookshow'),
    # URL for deleting contacts
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    # URL for deleting bookings
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),

    path('edit/<int:id>', views.edit, name='edit'),

    path('update/<int:id>', views.update,name='update'),

    path('uploadimage/', views.upload_image, name='upload'),

    path('showimage/', views.show_image, name='image'),

    path('imagedelete/<int:id>', views.imagedelete),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),



]
