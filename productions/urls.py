from django.urls import path
from .views import Productview, Productdetailview, Sendcomment

urlpatterns = [
    path('', Productview.as_view(), name='les'),
    path('<int:pk>/', Productdetailview.as_view(), name='detail'),
    path('<comment/int:pk>/', Sendcomment.as_view(), name='commenting'),
]
