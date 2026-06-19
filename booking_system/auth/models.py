from django.db import models


# Create your models here.
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

def login(requests):
    