from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CustomerViewSet, ProductViewSet, OrderViewSet, CartViewSet, CartItemViewSet, CommentViewSet, ReviewViewSet, PromoCodeViewSet, index, product_detail_view, about_view, add_to_cart, cart_detail, register, login_view, logout_view
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DRF Ecommerce API",
      default_version='v1',
      description="API documentation for the DRF Ecommerce project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@ecommerce.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'promocodes', PromoCodeViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('about/', about_view, name='about'),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('cart/', cart_detail, name='cart'),
    path('api/cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
