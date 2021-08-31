from django.contrib import admin

from django.urls import path, include

from anger import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change_don/', views.password_change_don, name='password_change_don'),
   
   

   
]
