from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    price = models.FloatField(null=False, default=9999.99)
    # TODO: add image field
    # TODO: add options field (e.g. sizes, color, etc.)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders',null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='item_orders', null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, related_name='order_items', null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingInformation(models.Model):
    customer = models.ForeignKey(Customer, related_name='shipping_info', null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, related_name='shipping_info', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    


    
    