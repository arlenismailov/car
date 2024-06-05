from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout, name='logout'),  # Используем функцию logout из views.py

    path('accounts/', include('allauth.urls')),
    path('products/', ProductView.as_view({'get': 'list', 'post': 'create'}), name='cars_list'),
    path('product/<int:pk>/', ProductView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='car_detail'),


]