

from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)                         # автологін після реєстрації
            messages.success(request, "Обліковий запис створено. Ласкаво просимо!")
            return redirect("core:rooms")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Ви успішно увійшли в систему.")
            return redirect("core:rooms")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})
