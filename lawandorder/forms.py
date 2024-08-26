from django import forms
from .models import Order


class Orderingform(forms):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes', ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'If you have a request(e.g about shipment) please make a not otherwise leave it empty'}),
        }
