from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def product(request, id):
    return render(request, 'product.html', {'id': id})

# Остальные функции, такие как register, login, logout и т.д.
