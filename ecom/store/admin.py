from django.contrib import admin, sites
from .models import Product, Category, Customer

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)