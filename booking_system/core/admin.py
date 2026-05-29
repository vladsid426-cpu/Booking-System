from django.contrib import admin
from .models import Booking,Room,RoomCategory,Review

# Register your models here.
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(RoomCategory)
admin.site.register(Review) 