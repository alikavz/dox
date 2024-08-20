from django.urls import path
from .views import cartdetails, addtocart, removing

app_name = 'cart'

urlpatterns = [
    path('', cartdetails, name='cartdetail'),
    path('add/<int:prod_id>', addtocart, name='sending'),
    path('remove/<int:prod_id>', removing, name='remove'),
]
