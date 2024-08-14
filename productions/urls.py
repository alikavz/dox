from django.urls import path
from .views import Productview, Productdetailview

urlpatterns = [
    path('', Productview.as_view(), name='les'),
    path('<int:pk>/', Productdetailview.as_view(), name='detail'),
]
