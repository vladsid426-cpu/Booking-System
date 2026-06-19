from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# 

app_name = 'core'

urlpatterns = [
    path('',views.home,name='home'),
    path("room",views.room_list, name="rooms"),
    path("room/<int:pk>",views.room_detail, name="room_detail"),

    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:pk>/", views.my_bookings, name="booking_detail"),
    path("bookings/<int:pk>/cancel/", views.booking_cancel, name="canceling"),

    # auth
    
]
'''path("accounts/login/",  auth_views.LoginView.as_view(template_name="core/auth/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", views.register, name="register"),'''
