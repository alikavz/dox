from django.shortcuts import render, redirect
from .forms import Orderingform
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Orderitems
from django.contrib import messages
from django.utils.translation import gettext as _


@login_required
def createorder(request):
    order_form = Orderingform
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('buy some stuff first!'))
        return redirect('les')

    if request.method == 'POST':
        order_form = Orderingform(request.POST, )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for items in cart:
                productsss = items['product_object']
                Orderitems.objects.create(
                    order=order_obj,
                    productsss=productsss,
                    quantity=items['quantity'],
                    price=productsss.price,
                )

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            messages.success(request, _('Thanks for your trust >3'))

    return render(request, 'lawandorder/orderdetail.html', {
        'form': order_form,
    })
