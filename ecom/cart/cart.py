from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in =product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities