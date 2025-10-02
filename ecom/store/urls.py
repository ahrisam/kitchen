from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_view/<int:pk>/', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),
    path('all_product/', views.all_product, name="all_product"),
]