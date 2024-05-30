from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CustomerViewSet, ProductViewSet, OrderViewSet, CartViewSet, CartItemViewSet, index, product_detail_view, about_view, add_to_cart, cart_detail, register

# Создаем роутер и регистрируем наши ViewSets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)

# Определяем список маршрутов
urlpatterns = [
    path('', index, name='index'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('about/', about_view, name='about'),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('logout/', include('djoser.urls.jwt')),
    path('accounts/', include('allauth.urls')),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('register/', register, name='register'),
]
