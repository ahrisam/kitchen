from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_add(request):
<<<<<<< HEAD
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id = product_id)
        cart_quantity = cart.__len__()

        cart.add(product=product)

        response = JsonResponse({'Product Name': product.name})
        return response

def cart_summary(request):
=======
>>>>>>> 05f27e4ccb813b14f871a2067d2d5dc9110c37de
    pass