from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                         # автологін після реєстрації
            messages.success(request, "Обліковий запис створено. Ласкаво просимо!")
            return redirect("core:room_list")
    else:
        form = UserCreationForm()
    return render(request, "core/auth/register.html", {"form": form})

@login_required
def my_bookings(request):
    """Список бронювань поточного користувача."""
    bookings = (
        Booking.objects.select_related("room", "room__category")
        .filter(user=request.user)
        .order_by("-created_at")
    )
    return render(request, "core/my_bookings.html", {"bookings": bookings})


@login_required
def booking_cancel(request, pk: int):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status != BookingStatus.CANCELED:
        booking.status = BookingStatus.CANCELED
        booking.save()
        messages.info(request, "Бронювання скасовано.")
    return redirect("core:my_bookings")