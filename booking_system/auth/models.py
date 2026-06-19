from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser

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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Ви успішно увійшли в систему.")
            return redirect("core:room_list")
    else:
        form = AuthenticationForm()
    return render(request, "core/auth/login.html", {"form": form})

