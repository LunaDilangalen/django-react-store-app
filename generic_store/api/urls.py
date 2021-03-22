from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerView)
router.register(r'products', views.ProductView)
router.register(r'orders', views.OrderView)
router.register(r'order_items', views.OrderItemView)
router.register(r'shipping_info', views.ShippingInformationView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
