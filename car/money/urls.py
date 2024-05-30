from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('products/', ProductView.as_view({'get': 'list'}), name='cars_list'),
    path('product/<int:pk>/', ProductView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car_detail'),


]