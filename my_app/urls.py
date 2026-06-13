from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/', views.get_users),
    path('api/v1/products/', views.get_products),
    path('api/v1/orders/', views.get_orders),
]