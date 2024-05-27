from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CustomerViewSet, ProductViewSet, OrderViewSet


urlpatterns = [
    path('', views.index, name='index'),
]
# Создаем роутер и регистрируем наши ViewSets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

# Определяем список маршрутов
urlpatterns = [
    path('', include(router.urls)),
]
