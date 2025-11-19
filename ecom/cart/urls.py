from django.urls import path
from . import views


urlpatterns = [
    path("add/", views.cart_add, name="cart_add"),
    path("summary/", views.cart_summary, name="cart_summary"),
    path("delete_cart/", views.cart_delete, name="cart_delete"),
    path("update/", views.cart_update, name='cart_update')
]