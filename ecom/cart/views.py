from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart
from store.models import Product
from django.contrib import messages

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    
    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'totals': totals,
    }
    return render(request, 'cart_summary.html', context)

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty', 1))
        
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, f"{product.name} added to cart!")
        return response
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = str(request.POST.get('product_id'))
        cart.delete(product=product_id)
        
        response = JsonResponse({
            'product': product_id,
            'qty': cart.__len__(),
        })
        messages.success(request, "Item removed from cart!")
        return response
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_update(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = str(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({
            'qty': product_qty,
            'total_qty': cart.__len__(),
        })
        messages.success(request, "Cart updated!")
        return response
    
    return JsonResponse({'error': 'Invalid request'}, status=400)