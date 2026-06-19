from django.shortcuts import get_object_or_404, redirect, render
from .models import Booking,Room,RoomCategory,BookingStatus
from reviews.models import Review
from .forms import BookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def room_list(requests):
    rooms = Room.objects.select_related("room_category").order_by("number")
    q = requests.GET.get("q", "").strip()
    cat = requests.GET.get("cat", "").strip()
    if q:
        rooms = rooms.filter(number__icontains=q)
    if cat:
        rooms = rooms.filter(category_id=cat)
    categories = RoomCategory.objects.filter(is_active=True).order_by("name")
    return render(requests, "room_list.html", {
        "rooms": rooms, "categories": categories, "q": q, "cat": cat
    })

@login_required
def room_detail(request, pk):
    room = get_object_or_404(Room.objects.select_related("room_category"), pk=pk)

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

    last_bookings = room.booking_set.select_related("user").order_by("-created_at")[:5]
    return render(request, "room_detail.html", {
        "room": room, "form": form, "last_bookings": last_bookings
    })



@login_required
def my_bookings(request):
    """Список бронювань поточного користувача."""
    bookings = (
        Booking.objects.select_related("room", "room__room_category")
        .filter(user=request.user)
        .order_by("-created_at")
    )
    return render(request, "my_booking.html", {"bookings": bookings})

@login_required
def booking_cancel(request, pk: int):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != BookingStatus.CANCELED:
        booking.status = BookingStatus.CANCELED
        booking.save()
        messages.info(request, "Бронювання скасовано.")
    return redirect("core:my_bookings")


def home(requests):

    return render(requests, "home.html")



    