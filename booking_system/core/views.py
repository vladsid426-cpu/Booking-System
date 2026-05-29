from django.shortcuts import render, get_object_or_404
from .models import Booking, Room, RoomCategory, Review

# Create your views here.
def room_list(requests):
    room_list = Room.objects.all()

    return render(requests,'room_list.html',{'room_list':room_list})

def review_list(requests):
    review_list = Review.objects.all()

    return render(requests,'review_list.html',{'review_list':review_list})

def review_detail(requests,id):
    review = get_object_or_404(Review,id=id)

    return render(requests,'review_detail.html',{'review_detail':review_detail})

def home(requests):
    room = Room.objects.all()
    review = Review.objects.all()

    return render(requests,'room_list.html',{'room_list':room,'review_list':review})