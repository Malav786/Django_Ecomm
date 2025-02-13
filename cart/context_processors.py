from .cart import Cart

# create context processor so our cart can be accessed in any template
def cart(request):
    return {'cart': Cart(request)}