from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='Home'),
    path('seller/',views.sellerpage, name='Seller'),
]