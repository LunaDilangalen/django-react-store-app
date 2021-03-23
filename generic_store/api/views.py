from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# TODO: look into difference of using generics.ListCreateAPIView, viewsets.ModelViewset, etc.
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = OrderItemSerializer

class ShippingInformationView(viewsets.ModelViewSet):
    queryset = ShippingInformation.objects.all().order_by('id')
    serializer_class = ShippingInformationSerializer

