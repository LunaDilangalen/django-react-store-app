from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
# TODO: look into difference of using generics.ListCreateAPIView, viewsets.ModelViewset, etc.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer