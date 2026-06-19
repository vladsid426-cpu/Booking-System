from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
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
    return render(request, "register.html", {"form": form})
