from django.shortcuts import render, redirect
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html',{'products': products,'categories':categories})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product':product})

# def category(request, foo):
#     foo = foo.replace('-', ' ')
#     caterogies = Category.objects.get(name=foo)
#     product = Category.objects.filter(caterogies)
#     return render(request, )