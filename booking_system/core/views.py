from .forms import BookingForm
from .models import Booking, Room, RoomCategory, Review, BookingStatus
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

# Create your views here.
def room_list(request):
    rooms = Room.objects.select_related("category").order_by("number")
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat", "").strip()
    if q:
        rooms = rooms.filter(number__icontains=q)
    if cat:
        rooms = rooms.filter(category_id=cat)
    categories = RoomCategory.objects.filter(is_active=True).order_by("name")
    return render(request, "core/room_list.html", {
        "rooms": rooms, "categories": categories, "q": q, "cat": cat
    })

def room_detail(requests,id):
    room = get_object_or_404(Room,id=id)

    return render(requests,'room_detail.html',{'room':room})

def review_list(requests):
    review_list = Review.objects.all()

    return render(requests,'review_list.html',{'review_list':review_list})

def room_detail(request, pk):
    room = get_object_or_404(Room.objects.select_related("category"), pk=pk)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Увійдіть, щоб забронювати кімнату.")
            return redirect("core:room_detail", pk=room.pk)

        # КЛЮЧ: одразу створюємо instance із room та user
        instance = Booking(room=room, user=request.user)
        form = BookingForm(request.POST, instance=instance)

        if form.is_valid():
            try:
                # model.save() → full_clean() → перевірка дат + перетинів
                with transaction.atomic():
                    form.save()
            except (ValidationError, IntegrityError) as e:
                # показуємо помилки моделі/БД у формі
                form.add_error(None, getattr(e, "message", str(e)))
            else:
                messages.success(request, "Бронювання створено! Очікує підтвердження.")
                return redirect("core:my_bookings")
    else:
        form = BookingForm()

    last_bookings = room.bookings.select_related("user").order_by("-created_at")[:5]
    return render(request, "core/room_detail.html", {
        "room": room, "form": form, "last_bookings": last_bookings
    })

def home(requests):
    room = Room.objects.all()
    review = Review.objects.all()

    return render(requests,'room_list.html',{'room_list':room,'review_list':review})

def my_bookings(request):
    bookings = (
        Booking.objects.select_related("room", "room__category")
        .filter(user=request.user)
        .order_by("-created_at")
    )
    return render(request, "core/my_bookings.html", {"bookings": bookings})

def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != BookingStatus.CANCELED:
        booking.status = BookingStatus.CANCELED
        booking.save()
        messages.info(request, "Бронювання скасовано.")
    return redirect("core:my_bookings")