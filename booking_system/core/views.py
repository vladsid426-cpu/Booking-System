from django.shortcuts import render
from .models import Booking, Room, RoomCategory

# Create your views here.
def room_list(requests):
    room_list = Room.objects.all()

    return render(requests,'room_list.html',{'room_list':room_list})
