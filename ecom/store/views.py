from django.shortcuts import render, redirect
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html',{'products': products,'categories':categories})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product':product})


def category(request, foo):
    foo = foo.replace('-', ' ')
    category = Category.objects.get(name=foo)
    products = Product.objects.filter(category=category)
    return render(request, "category.html", {'product': products, 'category':category})

def all_product(request):
    category = Category.objects.all().order_by('name')
    return render(request, 'all_products.html', {'category':category})