from django.db import models
from django.contrib.auth.models import User
import datetime

def get_default_user():
    return User.objects.get_or_create(username='default')[0].id

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=get_default_user)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    rating = models.FloatField(default=0)
    has_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, choices=[('card', 'Card'), ('cash', 'Cash')])
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.FloatField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.code

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
