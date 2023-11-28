from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CPUView(viewsets.ModelViewSet):
    queryset = ProductCPU.objects.all()
    serializer_class = ProductCPUSerializer


class GPUView(viewsets.ModelViewSet):
    queryset = ProductGPU.objects.all()
    serializer_class = ProductGPUSerializer


class RamView(viewsets.ModelViewSet):
    queryset = ProductRam.objects.all()
    serializer_class = ProductRamSerializer


class MemoryView(viewsets.ModelViewSet):
    queryset = ProductMemory.objects.all()
    serializer_class = ProductMemorySerializer


class DisplayView(viewsets.ModelViewSet):
    queryset = ProductDisplay.objects.all()
    serializer_class = ProductDisplaySerializer