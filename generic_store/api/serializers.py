from rest_framework import serializers
from .models import *

# TODO: look into differences of using ModelSerializer and HyperLinkedModelSerializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email') 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'date_ordered', 'complete', 'transaction_id')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'quantity', 'date_added')

class ShippingInformation(serializers.ModelSerializer):
    class Meta:
        model = ShippingInformation
        fields = ('order', 'customer', 'address', 'city', 'state', 'zipcode', 'date_added')


