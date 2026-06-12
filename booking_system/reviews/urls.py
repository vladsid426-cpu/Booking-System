from django.contrib import admin
from django.urls import path, include
from . import views
# 

app_name = 'reviews'

urlpatterns = [
    path('reviews',views.review_list, name="reviews"),
    path('reviews/<int:pk>',views.review_detail, name="review_detail"),


]