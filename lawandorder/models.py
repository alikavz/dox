from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is paid?'), default=False)

    first_name = models.CharField(_('First name'), max_length=60)
    last_name = models.CharField(_('Last name'), max_length=100)
    phone_number = models.CharField(_('Phone number'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)

    order_notes = models.CharField(_('Order notes'), max_length=700, blank=True)

    date_creation = models.DateTimeField(_('Create'), auto_now_add=True)
    date_modification = models.DateTimeField(_('Modify'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class Orderitems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    productt = models.ForeignKey('productions.Prod', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Order {self.id}: {self.productt} x {self.quantity} (price:{self.price}) '
