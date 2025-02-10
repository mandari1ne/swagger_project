from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('card/', views.cart_detail, name='cart_detail'),
    path('add/<int:film_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:film_id>/', views.cart_remove, name='cart_remove'),
]
