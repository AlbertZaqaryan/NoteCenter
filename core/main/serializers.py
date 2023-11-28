from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCPU
        fields = '__all__'

class ProductGPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGPU
        fields = '__all__'

class ProductRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRam
        fields = '__all__'

class ProductMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMemory
        fields = '__all__'

class ProductDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDisplay
        fields = '__all__'