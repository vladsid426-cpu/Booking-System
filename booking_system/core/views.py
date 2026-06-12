from django.shortcuts import get_object_or_404, redirect, render
from .models import Booking,Room,RoomCategory,Review
from .forms import BookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

# Create your views here.
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


def review_list(requests):
    review_list = Review.objects.all()

    return render(requests,'review_list.html',{'review_list':review_list})

def review_detail(requests,id:int):
    review = get_object_or_404(Review,id=id)

    return render(requests,'review_detail.html',{'review':review})

def home(requests):
    room = Room.objects.all()
    review = Review.objects.all()

    return render(requests,'home.html',{'room_list':room,'review_list':review})

def bookings(request):
    bookings = (
        Booking.objects.select_related("room", "room_category")
        .filter(user=request.user)
        .order_by("-created_at")
    )
    return render(request, "booking_list.html", {"bookings": bookings})

