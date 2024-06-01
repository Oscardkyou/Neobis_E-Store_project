from django.contrib import admin
from .models import Category, Customer, Product, Order, Cart, CartItem

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
