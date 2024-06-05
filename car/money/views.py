from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions, status
from .filters import ProductFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['brand', 'model']
    search_fields = ['title']
    filterset_class = ProductFilter


class CarorSparepartsView(viewsets.ModelViewSet):
    queryset = CarorSpareparts.objects.all()
    serializer_class = CarorSparepartsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ModelView(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    return Response('You can only see this if you are authenticated')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_and_blacklist_token(request):
    try:
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
