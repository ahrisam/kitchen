from django.urls import path
from . import views

urlpatterns = [
    path('', views.starter_page, name='starter_page')
]