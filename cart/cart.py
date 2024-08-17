from productions.models import Prod


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, productss, quantity=1):
        prod_id = str(productss.id)

        if prod_id not in self.cart:
            self.cart[prod_id] = {'quantity': quantity}
        else:
            self.cart[prod_id]['quantity'] += quantity

        self.save()

    def remove(self, productss):
        prod_id = str(productss.id)

        if prod_id in self.cart:
            del self.cart[prod_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        prod_ids = self.cart.keys()
        productsss = Prod.objects.filter(id__in=prod_ids)
        cart = self.cart.copy()

        for prodd in productsss:
            cart[str(productsss.id)]['product_object'] = prodd

        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']

    def get_total_price(self):
        prod_ids = self.cart.keys()
        productsss = Prod.objects.filter(id__in=prod_ids)
        return sum(product.price for product in productsss)
