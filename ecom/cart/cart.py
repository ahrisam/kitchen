from store.models import Product
from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price)
            }
        
        self.session.modified = True
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]['quantity'] = quantity
            else:
                del self.cart[product_id]
        
        self.session.modified = True
    
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
    
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        total = Decimal('0.00')
        
        for key, value in self.cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += Decimal(product.sale_price) * value['quantity']
                    else:
                        total += Decimal(product.price) * value['quantity']
        
        return total