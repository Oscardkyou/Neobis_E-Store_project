from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Customer, Product, Order
from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
