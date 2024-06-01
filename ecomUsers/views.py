from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Category, Customer, Product, Order, Cart, CartItem, Comment, Review, PromoCode
from .serializers import CategorySerializer, CustomerSerializer, ProductSerializer, OrderSerializer, CartSerializer, CartItemSerializer, CommentSerializer, ReviewSerializer, PromoCodeSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

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

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

# Новые классы ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = Comment.objects.filter(product=product)
    reviews = Review.objects.filter(product=product)
    return render(request, 'product_detail.html', {
        'product_detail': product,
        'comments': comments,
        'reviews': reviews,
    })

def about_view(request):
    return render(request, 'about.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'register.html')

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register2.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'success': True, 'cart_count': cart_count})

@login_required
def cart_detail(request):
    try:
        cart = get_object_or_404(Cart, user=request.user)
        return render(request, 'cart_detail.html', {'cart': cart})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)