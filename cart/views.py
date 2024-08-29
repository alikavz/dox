from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from django.views.decorators.http import require_POST
from .forms import Addtocart
from productions.models import Prod
from django.contrib import messages
from django.utils.translation import gettext as _


def cartdetails(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity'] = Addtocart(initial={
            'quantity': item['quantity'],
            'inplace': True
        })
    return render(request, 'cart/cartdetail.html', {
        'cart': cart
    })


@require_POST
def addtocart(request, prod_id):
    cart = Cart(request)
    productss = get_object_or_404(Prod, id=prod_id)
    form = Addtocart(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(productss, quantity, replacing=cleaned_data['inplace'])

    return redirect('cart:cartdetail')


def removing(request, prod_id):
    cart = Cart(request)
    productss = get_object_or_404(Prod, id=prod_id)
    cart.remove(productss)
    return redirect('cart:cartdetail')


@require_POST
def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('removed successfully!'))
    else:
        messages.warning(request, _('your cart is already empty!'))

    return redirect('les')
