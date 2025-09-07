from django.shortcuts import render, redirect
from . models import Product


def starter_page(request):
    products = Product.objects.all()
    return render(request, "index.html", {'product:': products})