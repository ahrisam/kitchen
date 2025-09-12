from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<str:foo>/', views.category, name='category')
]