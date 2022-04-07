from django import views
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product
from api import serializers

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>/',
        'Create': '/product-create/',
        'Update': '/product-detail/<int:id>/',
        'DElete': '/product-detail/<int:id>/',
    }
    return Response(api_urls);

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request, pk):
    product  = Product.objects.get(id=pk)
    serializers = ProductSerializer(instance=product, data=request.data)
    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

    
