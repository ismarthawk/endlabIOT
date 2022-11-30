from django.shortcuts import render

# Create your views here.
from .models import Product, Order


def home(request):

    context = {
        'products': Product.objects.all(),
    }
    return render(request, "ecart/home.html", context)
