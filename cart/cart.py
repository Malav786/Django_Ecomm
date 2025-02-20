from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        # get the current session key if it exists
        cart = self.session.get('session_key')
        # if it doesn't exist, create a new one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # make sure cart is available on all pages of the site
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

    def __len__(self):
        return len(self.cart) 
    
    def get_prods(self):
        # Get ids from the cart
        product_ids = self.cart.keys()
        # use ids to lookup products in the database
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        # Get ids from the cart
        quantities = self.cart
        return quantities
