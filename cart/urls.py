from django.urls import path
from .views import cartdetails, addtocart, removing, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', cartdetails, name='cartdetail'),
    path('add/<int:prod_id>', addtocart, name='sending'),
    path('remove/<int:prod_id>', removing, name='remove'),
    path('clear/', clear_cart, name='clear'),
]
