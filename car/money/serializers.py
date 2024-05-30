from rest_framework import serializers
from .models import *


class CarorSparepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarorSpareparts
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


