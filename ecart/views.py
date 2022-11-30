from django.shortcuts import render, redirect

# Create your views here.
from .models import Product, Order
from django.http import HttpResponse


def home(request):

    context = {
        'products': Product.objects.all(),
    }
    return render(request, "ecart/home.html", context)


def buy(request, productId):
    product = Product.objects.filter(id=productId).first()
    print(product)
    print(product.name)
    context = {
        'product': product
    }
    return render(request, 'ecart/buy.html', context)
