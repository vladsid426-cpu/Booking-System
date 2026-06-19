from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your models here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)                         # автологін після реєстрації
            messages.success(request, "Обліковий запис створено. Ласкаво просимо!")
            return redirect("core:room_list")
    else:
        form = UserCreationForm()
    return render(request, "core/auth/register.html", {"form": form})

def login_view(request):
    