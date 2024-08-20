from django.utils.translation import gettext as _
from django.contrib import messages
from productions.models import Prod


# we will send quantity and item to the html
class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, productss, quantity=1, replacing=False):
        prod_id = str(productss.id)

        if prod_id not in self.cart:
            self.cart[prod_id] = {'quantity': 0}

        if replacing:
            self.cart[prod_id]['quantity'] = quantity
        else:
            self.cart[prod_id]['quantity'] += quantity

        messages.success(self.request, _('added successfully'))
        self.save()

    def remove(self, productss):
        prod_id = str(productss.id)

        if prod_id in self.cart:
            del self.cart[prod_id]
            messages.success(self.request, _('removed successfully'))
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        prod_ids = self.cart.keys()
        productsss = Prod.objects.filter(id__in=prod_ids)
        cart = self.cart.copy()

        for prodd in productsss:
            cart[str(prodd.id)]['product_object'] = prodd

        for item in cart.values():
            item['total_price'] = item['product_object'].price * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']

    def get_total_price(self):
        prod_ids = self.cart.keys()

        return sum(item['quantity'] * item['product_object'].price for item in self.cart.values())
