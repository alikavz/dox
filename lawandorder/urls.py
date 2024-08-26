from django.urls import path
from .views import createorder

urlpatterns = [
    path('create/', createorder, name='ordering'),
]
