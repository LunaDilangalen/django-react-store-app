from rest_framework import serializers
from .models import *

# TODO: look into differences of using ModelSerializer and HyperLinkedModelSerializer
class ShippingInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInformation
        fields = ('order', 'customer', 'address', 'city', 'state', 'zipcode', 'date_added')

class ProductSerializer(serializers.ModelSerializer):
    item_orders = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='orderitem-detail'
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'item_orders')

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'quantity', 'date_added')

class OrderSerializer(serializers.ModelSerializer):
    shipping_info = ShippingInformationSerializer(many=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'date_ordered', 'complete', 'transaction_id', 'shipping_info', 'order_items')

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    shipping_info = ShippingInformationSerializer(many=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'orders', 'shipping_info')
        depth = 2 