from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('aboutus/', views.Aboutus.as_view(), name='about'),
]
