from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html',{'products': products,'categories':categories})

def product(request, pk):
    products = Product.objects.get(id=pk)
    return render(request, "product.html", {'product':products})
    product = Product.objects.get(id=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return render(request, "product.html", {'product':product, 'related_products':related_products})

def category(request, foo):
    foo = foo.replace('-', ' ')
    category = Category.objects.get(name=foo)
    products = Product.objects.filter(category=category)
    return render(request, "category.html", {'products': products, 'category':category})

def all_product(request):
    categories = Category.objects.all()
    product_by_category = {}
    for category in categories:
        product_by_category[category] = Product.objects.filter(category=category)
    print(product_by_category)
    return render(request, 'all_products.html',{'categories':categories, 'product_by_category':product_by_category})