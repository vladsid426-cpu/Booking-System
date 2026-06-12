from django.shortcuts import render
from .models import Review
from django.shortcuts import get_object_or_404, redirect, render
from .models import Review
from .forms import BookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

# Create your views here.
def review_list(requests):
    reviews = Review.objects.order_by("username")
    q = requests.GET.get("q", "").strip()
    cat = requests.GET.get("cat", "").strip()
    categories = ''
    return render(requests, "review_list.html", {
        "reviews": reviews, "categories": categories, "q": q, "cat": cat
    })
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    

    return render(request, "review_detail.html", {
        "review": review
    })
