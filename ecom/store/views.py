from django.shortcuts import render, redirect
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()


    return render(request, 'index.html',{'products': products,'categories':categories})

def category(request, foo):
    foo = foo.replace('-', ' ')
    category = Category.objects.get(name=foo)
    products = Product.objects.filter(category=category)

    return render(request, 'product.html', {'products':products, 'category':category })